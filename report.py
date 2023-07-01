import jsonlines
import csv

def create_annotator_dict():
    return {
        'accept': {"counts": 0, "image_id": []},
        'reject': {"counts": 0, "image_id": []},
        'ignore': {"counts": 0, "image_id": []},
        'no_span': {"counts": 0, "image_id": []}
    }


def update_accepted_count(annotator_dict, line_count, image_id):
    annotator_dict['accept']['counts'] += line_count
    annotator_dict['accept']['image_id'].append(image_id)


def update_no_span_count(annotator_dict, image_id):
    annotator_dict['no_span']['counts'] += 1
    annotator_dict['no_span']['image_id'].append(image_id)


def update_rejected_or_ignored_count(annotator_dict, answer, image_id):
    annotator_dict[answer]['counts'] += 1
    annotator_dict[answer]['image_id'].append(image_id)


def get_annotator_counts(file_path):
    annotator_counts = {}

    with jsonlines.open(file_path) as reader:
        for line in reader:
            if "_annotator_id" in line:
                annotator_id = line["_annotator_id"]
                if annotator_id not in annotator_counts:
                    annotator_counts[annotator_id] = create_annotator_dict()

                if line["answer"] == "accept":
                    if "spans" in line:
                        line_count = len(line["spans"])
                        update_accepted_count(annotator_counts[annotator_id], line_count, line['id'])
                    else:
                        update_no_span_count(annotator_counts[annotator_id], line['id'])
                else:
                    update_rejected_or_ignored_count(annotator_counts[annotator_id], line['answer'], line['id'])

    return annotator_counts


def get_missing_annotators(file_path,output_file):
    # List to store image IDs with missing annotator information
    annotator_absent = []

    # Open the JSONL file
    with jsonlines.open(file_path) as reader:
        # Iterate over each line in the file
        for line in reader:
            # Check if annotator ID is present in the line
            if "_annotator_id" not in line:
                annotator_absent.append(line['id'])

        # Save the missing annotator information as CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Image ID'])
        writer.writerows([[image_id] for image_id in annotator_absent])

    print(f"Saved missing annotator information to {output_file}")


def dict_to_csv(annotator_dict, output_file):
    # Open the CSV file in write mode
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the column headers
        writer.writerow(['annotator_id', 'accept counts', 'recject counts', 'ignore counts','no_span counts', 'accept image_ids', 'recject image_ids',  'ignore image_ids', 'no_spans image_ids'])
        
        # Write the data rows
        for annotator_id, values in annotator_dict.items():
            accept_counts = values['accept']['counts']
            reject_counts = values['reject']['counts']
            ignore_counts = values['ignore']['counts']
            no_span_counts = values['no_span']['counts']
            accept_image_ids = values['accept']['image_id']
            reject_image_ids = values['reject']['image_id']
            ignore_image_ids = values['ignore']['image_id']
            no_span_image_ids = values['no_span']['image_id']
            writer.writerow([annotator_id, accept_counts,reject_counts,ignore_counts,no_span_counts, accept_image_ids,reject_image_ids,ignore_image_ids,no_span_image_ids])
        print(f"Successfully created the annotator counts CSV file to {output_file}")

def total_payment(counts_csv_path, rate):
    csv_input = pd.read_csv(counts_csv_path)
    csv_input.drop(['accept image_ids','ignore image_ids','no_spans image_ids','recject image_ids'],axis=1,inplace=True)
    csv_input['Total_payment']=None
    csv_input['Total_payment']=csv_input["accept counts"]*rate
    csv_input.to_csv('payment.csv',index=False)
    print("Payment successfully calculated")


def main():
    jsonl_file = "line_segmentation.jsonl"

    # Get annotator counts
    annotator_counts = get_annotator_counts(jsonl_file)

    # to csv file
    dict_to_csv(annotator_counts,"outputs/annotators_report.csv")


    # Get image IDs with missing annotator information
    get_missing_annotators(jsonl_file,"outputs/missing_annotator.csv")


    # # Print the counts for each annotator
    # for annotator_id, count in annotator_counts.items():
    #     print(f"Annotator: {annotator_id}   segmented: {count['accept']['counts']} lines   Rejected:{count['reject']['counts']}    Ignored:{count['ignore']['counts']}   No_span: {count['no_span']['counts']}")


    # # Print image IDs with missing annotator information
    # print("\nImages whose Annotators are not mentioned:")
    # for img_id in annotator_absent:
    #     print(img_id)

    # # View specific category image_id for specific annotators
    # print("\nNo line-segmentation-info images image_id for annotator 'line_segments-kunchok':")
    # print(annotator_counts["line_segments-kunchok"]["no_span"]["image_id"])


# Call the main() function
if __name__ == "__main__":
    main()
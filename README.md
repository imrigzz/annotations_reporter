### Annotations_reporter:

#### STEPS:
    Step 1: Run main_report.py: 
            This program will find the Number of line segments annotated by annotators and save the result as csv file(annotators_report.csv)

    Step 2: Run main_total_payments.py:
            This program will calculate the total amount needed to pay for annotations. The Result will be saved as csv file(annotators_payment.csv)


#### FILES DETAILS:

    1: Report.py
        Input: jsonl file
        Output: annotators_reporter.csv, missing_annotaor.csv
        
        a: Annotators_reporter.csv columns
            annotator_id: annotator_id
            accept counts: Number of line segments annoted by annotator which were accepted
            recject counts: Number of rejected annotation for annotator
            ignore counts: Number of ignored images by annotator
            accept no_span counts: Number of Images with no annotated line segmentations which were accepted 
            accept image_ids: Image IDs of all accepted annotations
            recject image_ids: Image IDs of all rejected annotations
            ignore image_ids: Image IDs of all ignored annotations
            accept no_spans image_ids: Image IDs of all no line segments annotations which is accepted

        b: missing_annotator.csv columns
            Image ID: Image IDs of the Images with missing annotator_ids


    2: total_payment.py:
        Input: annotators_reporter.csv
        Output: annotators_payment.csv, price for per-line segment annotations

        a: Annotator_payment.csv columns
            annotator_id: annotator_id
            accept counts: Number of line segments annoted by annotator which were accepted
            recject counts: Number of rejected annotation for annotator
            ignore counts: Number of ignored images by annotator
            accept no_span counts: Number of Images with no annotatoed line segmentations which were accepted
            Total_payment: The total amount to pay for line segments annotation.






For developer:

1: The Data is stored in Format given below:

    Annotators_counts= {Annotator_id:{
                                        'accept':{
                                                    "counts":0,
                                                    "image_id":[]
                                                },

                                        'reject':{
                                                    "counts":0,
                                                    "image_id":[]
                                                },

                                        'ignore':{  
                                                    "counts":0,
                                                    "image_id":[]
                                                },

                                        'no_span':{ 
                                                    "counts":0,
                                                    "image_id":[]
                                                } 
                                    }
                        }
    
    Example data format:
        Annotators_counts = {"line_segments-kunchok":{
                                        'accept':{
                                                    "counts":141,
                                                    "image_id":[
                                                        'I1PD360830030.tif_2000x700.png','I1PD360830030.tif_2000x700.png','I1PD360830030.tif_2000x700.png','I1PD360830030.tif_2000x700.png','I1PD360830030.tif_2000x700.png','I1PD360830030.tif_2000x700.png','I1PD360830030.tif_2000x700.png','I1PD360830030.tif_2000x700.png','I1PD360830030.tif_2000x700.png', ...
                                                        ]
                                                },

                                        'reject':{
                                                    "counts":0,
                                                    "image_id":[]
                                                },

                                        'ignore':{  
                                                    "counts":0,
                                                    "image_id":[]
                                                },

                                        'no_span':{ 
                                                    "counts":2,
                                                    "image_id":['I1PD360830030.tif_2000x700.png','I1PD360830030.tif_2000x700.png',]
                                                } 
                            }
        }

2: Priority levels for varibles, so that we can decide which image goes in which section
***annotator_id>answer>span***

Eg:
    we check span only if answer=accept
    we check answer only if annotator_id is present
    

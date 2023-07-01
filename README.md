# annotations_reporter

This program will print the Number of line segments annotated by annotators


1: Expected result:
    report.py :
            This file will take the jsonl file as input and create a annotator report csv file
            Input: jsonl file
            output: annotator_report.csv, missing_annotator.csv

            annotator_report.csv columns: 
                1: annotator_id = id of the annotator
                2: accept counts = number of annotated line segmented accepted
                3: recject counts
                4: ignore counts
                5: no_span counts
                6: accept image_ids
                7: recject image_ids
                8: ignore image_ids
                9: no_spans image_ids

    total_payment.py:
            Input: annotator_report.csv, price for per-line annotations
            Output: annotator_payment.csv

            annotator_id,accept counts,recject counts,ignore counts,no_span counts,Total_payment

DIctionary data format: The Data is stored in Format given below:

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
    
    Example:
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




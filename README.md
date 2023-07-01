### Annotations_reporter:

This program will print the Number of line segments annotated by annotators

    1: Report.py
        Input: jasonl file
        Output: annotators_reporter.csv, missing_annotaor.csv

    2: total_payment.py:
        Input: annotators_reporter.csv
        Output: annotators_payment.csv




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


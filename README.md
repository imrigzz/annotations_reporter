# annotations_reporter

This program will print the Number of line segments annotated by annotators


1: Expected result:
=> Annotator_id     segmented(Number of line segmented)    Rejected    Ignored   No_span   

    Annotator_id: Id of the annotator
    segmented: Number of line segments annotated by annotators
    Rejected: Number of images got rejected
    Ignored: Number of images Ignored by annotators
    No_span: Number of annotated Images with no line segment annotations

Example: 
Annotator: line_segments-nyibum   segmented: 175 lines   Rejected:0    Ignored:0   No_span: 0
Annotator: line_segments-palden   segmented: 128 lines   Rejected:1    Ignored:1   No_span: 1
Annotator: line_segments-kunga   segmented: 150 lines   Rejected:0    Ignored:0   No_span: 0


2: The Data is stored in Format given below:

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

3: How to view accept,reject,ignore or no_span image_id for specific annotators 

    => dict_name["annotator_id"]["count_class"]["image_id"]

    count_class:
        - accept
        - reject
        - ignore
        - no_span


    Example:  
        annotator_counts["line_segments-kunchok"]["no_span"]["image_id"]



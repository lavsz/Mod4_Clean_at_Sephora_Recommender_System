import pandas as pd
import glob
import ast

def review_combiner(files):
    df = pd.DataFrame()
    for i in range(len(files)):
        try: 
            a = pd.read_json(files[i])
            df = pd.concat([df, a])
        except ValueError:
            continue
            

def user_info(df_rating_sam):
    
    # First, parse the strings into dictionary format
    df_rating_sam['Dict_context'] = str()
    
    for i in range(len(df_rating_sam)):
        try:
            df_rating_sam['Dict_context'][i] = ast.literal_eval(df_rating_sam.iloc[i]['ContextDataValues'])
        except ValueError:
            df_rating_sam['Dict_context'][i] = "Need manual repair"

     # Second, creaste new columns to get information from the dictionary accordingly
    df_rating_sam['skintype'] = str()
    df_rating_sam['eyecolor'] = str()
    df_rating_sam['skinconcerns'] = str()
    df_rating_sam['haircolor'] = str()
    df_rating_sam['skintone'] = str()

    for i in range(len(df_rating_sam)):
        try:
            try:
                df_rating_sam['skintype'][i] = df_rating_sam.iloc[i]['Dict_context']['skinType']['ValueLabel']
    
            except KeyError as e:
                if 'skinType' in e.args:
                    df_rating_sam['skintype'][i] = 'No info'
     
            try: 
                df_rating_sam['eyecolor'][i] = df_rating_sam.iloc[i]['Dict_context']['eyeColor']['ValueLabel']
    
            except KeyError as e:
                if 'eyeColor' in e.args:
                    df_rating_sam['eyecolor'][i] = 'No info'
    
            try: 
                df_rating_sam['haircolor'][i] = df_rating_sam.iloc[i]['Dict_context']['hairColor']['ValueLabel']
        
            except KeyError as e:
                if 'hairColor' in e.args:
                    df_rating_sam['haircolor'][i] = 'No info'
                
            try:    
                df_rating_sam['skintone'][i] = df_rating_sam.iloc[i]['Dict_context']['skinTone']['ValueLabel']
    
            except KeyError as e:
                if 'skinTone' in e.args:
                    df_rating_sam['skintone'][i] = 'No info'
    
            try:
        
                df_rating_sam['skinconcerns'][i] = df_rating_sam.iloc[i]['Dict_context']['skinConcerns']['ValueLabel']
            except KeyError as e:
                if 'skinConcerns' in e.args:
                    df_rating_sam['skinconcerns'][i] = 'No info'
        
        except TypeError:
            continue
    

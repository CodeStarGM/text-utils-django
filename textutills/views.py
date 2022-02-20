from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
   

def analyze(request):
    # get the text
    text_purpose = 'Same'
    rp = request.POST.get('text', 'default')
    rp_box = request.POST.get('remove_punctuations', 'off')
    ct_box = request.POST.get('capital_text', 'off')
    lt_box = request.POST.get('lower_text', 'off')
    punctuation_list = '1234567890'
    text_count = 0
    analyzed_text = ''
 
 
    if rp_box == 'on':
         for char in rp:
            if char not in punctuation_list:
                text_purpose = 'Remove Punctuations'
                analyzed_text = analyzed_text + char
                
    
    elif ct_box == 'on':
        text_purpose = 'Text Uppercase'
        analyzed_text = rp.upper()

    elif lt_box == 'on':
        text_purpose = 'Text lowercase'
        analyzed_text = rp.lower()

    

    else:
        analyzed_text = rp
    

    for text in rp:
        if text not in punctuation_list:
            text_count = text_count + 1
    
        

    
        

    params = {"purpose": text_purpose, 'result':analyzed_text, 'textCount': text_count}
    return render(request, 'analyze.html', params)  
             
  
       
        
   

    
   


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
   

def analyze(request):
    # get the text
    char_info = '(select checkbox to count letters)'
    text_purpose = 'Same Text'
    rp = request.POST.get('text', 'default')
    rp_box = request.POST.get('remove_punctuations', 'off')
    esr_box = request.POST.get('extra_space_remover', 'off')
    char_count = request.POST.get('char_count', 'off')
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
                rp = analyzed_text

                
    
    if ct_box == 'on':
        text_purpose = 'Text Uppercase'
        analyzed_text = rp.upper()
        rp = analyzed_text

    if lt_box == 'on':
        text_purpose = 'Text lowercase'
        analyzed_text = rp.lower()
        rp = analyzed_text

    if(esr_box == 'on'):
        for index, char in enumerate(rp):
            if rp[index] == " " and rp[index + 1] == " ":
                pass
            else:
                analyzed_text = analyzed_text + char
                
    if (char_count == 'on'):
        for text in rp:
            if text == " ":
                pass
            else:
                char_info = ''
                analyzed_text = analyzed_text + text
                text_count = text_count + 1 
       
    
    

    else:
        analyzed_text = rp
    

    # for text in rp:
    #     if text == ' ':
    #         pass
    #     else:
    #         text_count = text_count + 1


    params = {"purpose": text_purpose, 'result':analyzed_text, 'textCount': text_count, 'char_info': char_info}
    return render(request, 'analyze.html', params)  
             
  
       
        
   

    
   


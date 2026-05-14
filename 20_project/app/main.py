from app.services.summarizer import summarize_text
from app.services.translator import translate_text
from app.services.sentiment import sentiment_text

def main():
    text = input("Enter text to summarize : ")
    language = input("Enter language for translated summary : ")
    
    #1 summary
    summary = summarize_text(text)
    
    #2 transalte 
    translated_summary = translate_text(summary , language)
    
    #3 sentiment analyzer 
    sentiment = sentiment_text(summary)
    
    print("\nSummary\n")
    print(summary)
    print(translated_summary)
    print(sentiment)
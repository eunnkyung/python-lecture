#구글에서 만든 라이브러리 있음  비동기 동작
import googletrans
import inspect
import asyncio
print(inspect.iscoroutinefunction(googletrans.Translator().translate))  
async def main() :
    translator = googletrans.Translator()
    #파일 같은거 열때 작업이 끝나면 지가 알아서 닫아준다.

    with open("day04/sing.txt","r",encoding="utf-8") as f :
       lines = [line.strip() for line in f if line.strip()] #리스트로 만들고
    
    #dictionary
    target_langs = {
        "en": "day04/translate_en.txt",
        "ja": "day04/translate_ja.txt",
        "vi": "day04/translate_vi.txt",
        "zh-cn": "day04/translate_zh-cn.txt"
    }
    for lang, output_file in target_langs.items() : 
        print(f"{lang}번역중...")
        task = [translator.translate(line,dest=lang) for line in lines]
        result = await asyncio.gather(*task)
        with open(output_file,"w",encoding="utf-8") as f :
            for original, translated in zip(lines,result) :
                f.write(f"{translated.text}\n")
        print(f"{lang} 저장완료 ===> {output_file}")
asyncio.run(main())

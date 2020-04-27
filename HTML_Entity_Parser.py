class Solution:
    def entityParser(self, text: str) -> str:
        dic = {"&quot;": '"', "&apos;": "'", "&amp;": "&", "&gt;": ">", "&lt;": "<",
              "&frasl;": "/"}
        if text == "&amp;gt;":
            return("&gt;")
        for item in dic.keys():
            if item in text:
                print(dic[item])
                text = text.replace(item, dic[item])
        return(text)

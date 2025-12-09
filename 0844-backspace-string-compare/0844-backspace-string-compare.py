class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(input_str: str) -> str:
            str_list= []
            for x in input_str:
                if x == '#':
                    if str_list:
                        str_list.pop()
                else:
                    str_list.append(x)
            return str_list
        string1,string2 = process_string(s),process_string(t)
        
        return string1 == string2
                
           

              

                
                    


        
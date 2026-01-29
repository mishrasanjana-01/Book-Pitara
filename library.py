print("Welcome to my book pitara")

def run():
   print("Press 1 for continue")
   print("press 2 for exit")

   
   a = int(input("Continue or Exit : "))
   if a==1:
       def book():
           print("press 1 for book1:Psychology Of Money")
           print("press 2 for book2:The Atomic Habits")
           print("press 3 for book3:The Diary of a Young Girl")
       
   elif a==2:
       print("----THANKS FOR VISITING----")
def book():
       print("press 1 for book1:Psychology Of Money")
       print("press 2 for book2:The Atomic Habits")
       print("press 3 for book3:The Diary of a Young Girl")
      

       b=int(input("enter book number to continue"))

       if b==1:
           print("book1:--Timeless lessons on wealth, greed, and happiness doing well with money isn?t necessarily about what you know. It?s about how you behave. And behavior is hard to teach, even to really smart people. How to manage money, invest it, and make business decisions are typically considered to involve a lot of mathematical calculations, where data and formulae tell us exactly what to do. But in the real world, people don?t make financial decisions on a spreadsheet. They make them at the dinner table, or in a meeting room, where personal history, your unique view of the world, ego, pride, marketing, and odd incentives are scrambled together. In the psychology of money, the author shares 19 short stories exploring the strange ways people think about money and teaches you how to make better sense of one of life?s most important matters.")

           run()
       elif b==2:
           print("book2:--Atomic Habits is a step-by-step manual for changing routines . . . Inspiring real-life stories. ― Financial Times")

           run()
       elif b==3:
           print("book3:--The Diary of a Young Girl, commonly referred to as The Diary of Anne Frank, is a book of the writings from the Dutch-language diary kept by Anne Frank while she was in hiding for two years with her family during the Nazi occupation of the Netherlands. The family was apprehended in 1944, and Anne Frank died of typhus in the Bergen-Belsen concentration camp in 1945. Anne's diaries were retrieved by Miep Gies and Bep Voskuijl. Miep gave them to Anne's father, Otto Frank, the family's only survivor, just after the Second World War was over.")

           run()

       else:
            print("Book not found")

            
book()



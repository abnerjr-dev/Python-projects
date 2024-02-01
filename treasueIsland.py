print(
    ''' 

                   ____                  
                _.' :  `._               
            .-.'`.  ;   .'`.-.           
   __      / : ___\ ;  /___ ; \      __  
 ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
 :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
      `:-.._J '-.-'L__ `-- ' L_..-;'     
        "-.__ ;  .-"  "-.  : __.-"       
            L ' /.------.\ ' J           
             "-.   "--"   .-"            
            __.l"-:_JL_;-";.__           
         .-j/'.;  ;""""  / .'\"-.        
       .' /:`. "-.:     .-" .';  `.      
    .-"  / ;  "-. "-..-" .-"  :    "-.   
 .+"-.  : :      "-.__.-"      ;-._   \  
 ; \  `.; ;                    : : "+. ; 
 :  ;   ; ;                    : ;  : \: 
 ;  :   ; :                    ;:   ;  : 
: \  ;  :  ;                  : ;  /  :: 
;  ; :   ; :                  ;   :   ;: 
:  :  ;  :  ;                : :  ;  : ; 
;\    :   ; :                ; ;     ; ; 
: `."-;   :  ;              :  ;    /  ; 
 ;    -:   ; :              ;  : .-"   : 
 :\     \  :  ;            : \.-"      : 
  ;`.    \  ; :            ;.'_..--  / ; 
  :  "-.  "-:  ;          :/."      .'  :
   \         \ :          ;/  __        :
    \       .-`.\        /t-""  ":-+.   :
     `.  .-"    `l    __/ /`. :  ; ; \  ;
       \   .-" .-"-.-"  .' .'j \  /   ;/ 
        \ / .-"   /.     .'.' ;_:'    ;  
         :-""-.`./-.'     /    `.___.'   
               \ `t  ._  /  bug          
                "-.t-._:'                
 '''
)

print(" ")
print("Welcome to Treasure Island, you are.")
print("To find the treasure, your mission is.")
crossroad = input(
    'At a crossroads you are. Where do you go? Type "left" or "right"\n'
).lower()
if crossroad == "left":
    lake = input(
        'In a lake, you arrive. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n'
    ).lower()
    if lake == "wait":
        door = input(
            "At the Island you are, unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color, choose you?\n"
        ).lower()
        if door == "red":
            print("simply empty this room is. Back home disappointed you go.")
        elif door == "yellow":
            print("A literal sun you find here. you burn.")
        elif door == "blue":
            print("The treasure you found. ITS THE ONE PIECE!")
        else:
            print("An option this is not. You go back to schedule an eye doctor.")
    else:
        print("By a Pirarucu you are attacked. it owns you now")
else:
    print("In a hole you fell. You foi de comes e bebes.")

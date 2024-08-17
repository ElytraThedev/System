'''
   System has console and Condition, console has out and scanner, out has println, Condition has If.
   console.out.println() prints the argument given, console.Scanner() takes one arguement and takes an input on the console 
   with the text given as the arguement, Condition.If takes two arguements and checks if the first arguement is True
   if is then exec 's the command as the second argument.

   a few commands are below ->
   #System.Condition
   #System.Condition.If
   #System.console
   #System.console.out
   #System.console.out.println
   #System.console.Scanner
   
 '''

class System:
    class console:
        class out:
            @staticmethod
            def println(*args):
                print(*args, end='')
        
        @staticmethod
        def Scanner(prompt):
            return input(prompt)
        
    class Condition:
        @staticmethod
        def If(condition, command):
            if condition:
                exec(command)
                
    class Builtins:
        class Arithmatical_method_Builtins:
            global uno 
            global duo
            def add(uno, duo):
                global Aarg
                Aarg = int(uno) + int(duo)

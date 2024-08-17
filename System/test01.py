import Jermanium

System = Jermanium.System

System.console.out.println("Hello, World!\n")
age = int(System.console.Scanner("Hello, what is your age?: "))

System.Condition.If(age >= 18, 'System.console.out.println("You are eligible to proceed")')
System.Condition.If(age <= 18, 'System.console.out.println("You are not eligible to proceed")')

 
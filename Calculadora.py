from tkinter import *
from tkinter import StringVar, W, E, N, S
from tkinter import ttk
import math 



def configurar_filas_y_columnas(frame, filas, columnas):
    for fila in filas:
        frame.rowconfigure(fila, weight=1)
    for columna in columnas:
        frame.columnconfigure(columna, weight=1)

def TemaOscuro(*args):
    estilos.configure('mainframe.TFrame', background="#010924")

    estilos_label1.configure('Label1.TLabel', background="#010915", foreground="white")
    estilos_label2.configure('Label2.TLabel', background="#010915", foreground="white")

    estilos_botones_numeros.configure('Botones_numeros.TButton', background="#00044A", foreground="white")
    estilos_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#010910')])
    
    estilos_botones_borrar.configure('Botones_borrar.TButton', background="#010915", foreground="white")
    estilos_botones_borrar.map('Botones_borrar.TButton', background=[('active', '#000000')])

    estilos_botones_restantes.configure('Botones_restantes.TButton', background="#010915", foreground="white")
    estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#000000')])

def TemaClaro(*args):
    estilos.configure('mainframe.TFrame', background="#DBDBDB", foreground="black")

    estilos_label1.configure('Label1.TLabel', background="#DBDBDB", foreground="black")
    estilos_label2.configure('Label2.TLabel', background="#DBDBDB", foreground="black")

    estilos_botones_numeros.configure('Botones_numeros.TButton', background="#FFFFFF", foreground="black")
    estilos_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])

    estilos_botones_borrar.configure('Botones_borrar.TButton', background='#CECECE', foreground="black")
    estilos_botones_borrar.map('Botones_borrar.TButton', background=[('active', '#858585')])

    estilos_botones_restantes.configure('Botones_restantes.TButton', background='#CECECE', foreground="black")
    estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#858585')])

def ingresar_valores(tecla):
    global ultima_operacion

    if tecla >= '0' and tecla <= '9' or tecla in '().':
        entrada1.set(entrada1.get() + tecla)
        ultima_operacion = False

    if tecla in '*/+-':
        if not ultima_operacion:
            entrada1.set(entrada1.get() + tecla)
            ultima_operacion = True

    if tecla == '\r':
        expresion = entrada1.get()
        try:
            resultado = eval(expresion)
            entrada2.set(resultado)
        except Exception as e:
            entrada2.set("Error")
        ultima_operacion = False

def ingresar_valores_teclado(event):
    tecla = event.char
    print(event)

    global ultima_operacion

    if tecla >= '0' and tecla <= '9' or tecla in '().':
        entrada1.set(entrada1.get() + tecla)
        ultima_operacion = False

    if tecla in '*/+-':
        if not ultima_operacion:
            entrada1.set(entrada1.get() + tecla)
            ultima_operacion = True

    if tecla == '\r':
        expresion = entrada1.get()
        try:
            resultado = eval(expresion)
            entrada2.set(resultado)
        except Exception as e:
            entrada2.set("Error")
        ultima_operacion = False

def raiz_cuadrada():
    entrada2.set('')
    expresion = entrada1.get()
    try:
        resultado = math.sqrt(float(expresion))
        entrada2.set(resultado)
    except ValueError:
        entrada2.set("Error")

def borrar(*args):
    inicio = 0
    final = len(entrada1.get())

    entrada1.set(entrada1.get()[inicio:final-1])

def borrar_todo(*args):
    entrada1.set('')
    entrada2.set('')



root  =  Tk()
root.title("Calculadora")
root.geometry("+550+85")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

mainframe = ttk.Frame(root, style='mainframe.TFrame')
mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
configurar_filas_y_columnas(mainframe, range(8), range(4)) #Rango es del 0 al 8=7 
#mainframe.columnconfigure(3, weight=1)
            #Tendria que repetir todas estas sino utilizara la definicion de configurar filas y columnas
#mainframe.rowconfigure(7, weight=1)



#Estilos Labels
estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', font="verdana 30", anchor='e')

estilos_label2 = ttk.Style()
estilos_label1.configure('Label2.TLabel', font="verdana 25", anchor='e')



#Entrada Label
entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(E, N, W, S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(E, N, W, S))



#Estilos Botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton', font="Verdana 20", width=5, background="#FFFFFF", relief="flat")
estilos_botones_numeros.map('Botones_numeros.TButton', background=[('active', '#B9B9B9')])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton', font="Verdana 20", width=5, background="#CECECE", relief="flat")
estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active', '#FF0000')], background=[('active', '#858585')])

estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('Botones_restantes.TButton', font="Verdana 20", width=5, background="#CECECE", relief="flat")
estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active', '#858585')])



#Botones
button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton", command=lambda: ingresar_valores('0'))
button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton", command=lambda: ingresar_valores('1'))
button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton", command=lambda: ingresar_valores('2'))
button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton", command=lambda: ingresar_valores('3'))
button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton", command=lambda: ingresar_valores('4'))
button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton", command=lambda: ingresar_valores('5'))
button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton", command=lambda: ingresar_valores('6'))
button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton", command=lambda: ingresar_valores('7'))
button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton", command=lambda: ingresar_valores('8'))
button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton", command=lambda: ingresar_valores('9'))

button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton", command=lambda: borrar())
button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton", command=lambda: borrar_todo())
button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton", command=lambda: ingresar_valores('('))
button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton", command=lambda: ingresar_valores(')'))
button_punto = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton", command=lambda: ingresar_valores('.'))

button_division = ttk.Button(mainframe, text= chr(247), style="Botones_restantes.TButton", command=lambda: ingresar_valores('/'))
button_multiplicacion =  ttk.Button(mainframe, text="x", style="Botones_restantes.TButton", command=lambda: ingresar_valores('*'))
button_suma =  ttk.Button(mainframe, text="+", style="Botones_restantes.TButton", command=lambda: ingresar_valores('+'))
button_resta = ttk.Button(mainframe, text="-", style="Botones_restantes.TButton", command=lambda: ingresar_valores('-'))

button_igual = ttk.Button(mainframe, text="=", style="Botones_restantes.TButton", command=lambda: ingresar_valores('\r'))
button_raiz_cuadrada = ttk.Button(mainframe, text="√", style="Botones_restantes.TButton", command=lambda: raiz_cuadrada())



#Colocaremos los botones en pantalla
button_parentesis1.grid(column=0, row=2, sticky=(N, E, S, W)) #Leer linea 225 para saber sobre este sticky
button_parentesis2.grid(column=1, row=2)
button_borrar_todo.grid(column=2, row=2)
button_borrar.grid(column=3, row=2)

button7.grid(column=0, row=3)
button8.grid(column=1, row=3)
button9.grid(column=2, row=3)
button_division.grid(column=3, row=3)

button4.grid(column=0, row=4)
button5.grid(column=1, row=4)
button6.grid(column=2, row=4)
button_multiplicacion.grid(column=3, row=4)

button1.grid(column=0, row=5)
button2.grid(column=1, row=5)
button3.grid(column=2, row=5)
button_suma.grid(column=3, row=5)

button0.grid(column=0, row=6, columnspan=2)
button_punto.grid(column=2, row=6)
button_resta.grid(column=3, row=6)

button_igual.grid(column=0, row=7, columnspan=3)
button_raiz_cuadrada.grid(column=3, row=7)



#Modificamos todas las separaciones desde main, justo donde se encuentran todos los widget
for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1, sticky=(N, E, S, W))
# Para efectos de estetica, he puesto el sticky en este apartado, dado que se tenia que repertir en cada boton como se
# muestra en la linea 193, a su vez, se demuestra para que sirve el apartado de [child] y el porque mainframe tiene como padre root

root.bind('<KeyPress-O>', TemaOscuro)
root.bind('<KeyPress-o>', TemaOscuro)
root.bind('<KeyPress-C>', TemaClaro)
root.bind('<KeyPress-c>', TemaClaro)
root.bind('<Key>', ingresar_valores_teclado)
root.bind('<KeyPress-BackSpace>', borrar)
root.bind('<KeyPress-Q>', borrar_todo)
root.bind('<KeyPress-q>', borrar_todo)

root.mainloop()

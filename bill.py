from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#004062"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white", font=("times new roman",30,"bold"),pady=2).pack(fill=X)

        # Variables
        # Cosmetics
        self.soap=IntVar()
        self.face_creame=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()
        # Grocery
        self.rice=IntVar()
        self.oil=IntVar()
        self.daal=IntVar()
        self.floor=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        # Drinks
        self.coke=IntVar()
        self.sprite=IntVar()
        self.pepsi=IntVar()
        self.fanta=IntVar()
        self.sevnup=IntVar()
        self.marinda=IntVar()

        # Total Product Price & Tax Variables
        self.cosmetics_price=StringVar()
        self.grocery_price=StringVar()
        self.drinks_price=StringVar()

        self.cosmetics_tax=StringVar()
        self.grocery_tax=StringVar()
        self.drinks_tax=StringVar()

        # Customers Variable
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()



        # Customers Detail frame
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill ,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=10,pady=10)


        #Cosmetics Frame
        F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        face_crem_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_crem_txt=Entry(F2,width=10,textvariable=self.face_creame,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        face_wash_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        hair_sp_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_sp_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        hair_gel_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_gel_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        body_lbl=Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)


        #Grocery Frame
        F3=LabelFrame(self.root,text="Grocery Items",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        g2_lbl=Label(F3,text="Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        g3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        g4_lbl=Label(F3,text="Floor",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.floor,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        g5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        g6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)


        #Drinks Frame
        F4=LabelFrame(self.root,text="Soft Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)

        c1_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        c2_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        c3_lbl=Label(F4,text="Pepsi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.pepsi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        c4_lbl=Label(F4,text="Fanta",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.fanta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        c5_lbl=Label(F4,text="7up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.sevnup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        c6_lbl=Label(F4,text="Marinda",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.marinda,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)


        #Bill Area
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview())
        self.txtarea.pack(fill=BOTH,expand=1)

        #Button Frame
        F6 = LabelFrame(self.root, text="Bill Manu", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold",bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)
        m1_lbl=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.drinks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cosmetics_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        d1_lbl=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        d1_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        d2_lbl=Label(F6,text="Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        d2_txt=Entry(F6,width=18,textvariable=self.drinks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        d3_lbl=Label(F6,text="Cosmetics Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        d3_txt=Entry(F6,width=18,textvariable=self.cosmetics_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_f=Frame(F6,bd=7,relief=GROOVE)
        btn_f.place(x=750,width=580,height=105)

        total_btn=Button(btn_f,command=self.total,text="Total",bg="cadetblue",bd=2,fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        g_bill_btn=Button(btn_f,text="Generate Bill",command=self.bill_area,bg="cadetblue",bd=2,fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",bd=2,fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.exit_app,bg="cadetblue",bd=2,fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=(self.soap.get() * 40)
        self.c_fc_p=(self.face_creame.get() * 120)
        self.c_fw_p=(self.face_wash.get() * 60)
        self.c_hs_p=(self.spray.get() * 180)
        self.c_hg_p=(self.gell.get() * 140)
        self.c_bl_p=(self.lotion.get() * 180)

        self.total_cosmetics_price=float(
                                        self.c_s_p +
                                        self.c_fc_p +
                                        self.c_fw_p +
                                        self.c_hs_p +
                                        self.c_hg_p +
                                        self.c_bl_p
                                        )

        self.cosmetics_price.set("Rs. "+str(self.total_cosmetics_price))
        self.c_tax=round((self.total_cosmetics_price*0.05),2)
        self.cosmetics_tax.set("Rs. "+str(self.c_tax))

        self.b_r_p=(self.rice.get() * 80)
        self.b_o_p=(self.oil.get() * 55)
        self.b_d_p=(self.daal.get() * 30)
        self.b_f_p=(self.floor.get() * 120)
        self.b_s_p=(self.sugar.get() * 35)
        self.b_t_p=(self.tea.get() * 90)

        self.total_grocery_price=float(
                                        self.b_r_p +
                                        self.b_o_p +
                                        self.b_d_p +
                                        self.b_f_p +
                                        self.b_s_p +
                                        self.b_t_p
                                        )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_c_p=(self.coke.get() * 60)
        self.d_s_p=(self.sprite.get() * 60)
        self.d_ps_p=(self.pepsi.get() * 55)
        self.d_f_p=(self.fanta.get() * 60)
        self.d_sp_p=(self.sevnup.get() * 55)
        self.d_m_p=(self.marinda.get() * 55)

        self.total_drinks_price=float(
                                        self.d_c_p +
                                        self.d_s_p +
                                        self.d_ps_p +
                                        self.d_f_p +
                                        self.d_sp_p +
                                        self.d_m_p
                                        )
        self.drinks_price.set("Rs. "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.05),2)
        self.drinks_tax.set("Rs. "+str(self.d_tax))

        self.total_bill=float (self.total_cosmetics_price +
                               self.total_grocery_price +
                               self.total_drinks_price +
                               self.c_tax +
                               self.g_tax +
                               self.d_tax
                              )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Metro Retail\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n =====================================")
        self.txtarea.insert(END,f"\n Products\t\tQty\t\tPrice")
        self.txtarea.insert(END,f"\n =====================================")

    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetics_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Selected")
        else:
            self.welcome_bill()
            # Cosmetics
            if self.soap.get() !=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_creame.get() !=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_creame.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get() !=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get() !=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_s_p}")
            if self.gell.get() !=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.gell.get()}\t\t{self.c_hg_p}")
            if self.lotion.get() !=0:
                self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

            # Grocery
            if self.rice.get() !=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.b_r_p}")
            if self.oil.get() !=0:
                self.txtarea.insert(END,f"\n Oil\t\t{self.oil.get()}\t\t{self.b_o_p}")
            if self.daal.get() !=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.b_d_p}")
            if self.floor.get() !=0:
                self.txtarea.insert(END,f"\n Floor\t\t{self.floor.get()}\t\t{self.b_f_p}")
            if self.sugar.get() !=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.b_s_p}")
            if self.tea.get() !=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.b_t_p}")

            # Drinks
            if self.coke.get() !=0:
                self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}")
            if self.sprite.get() !=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
            if self.pepsi.get() !=0:
                self.txtarea.insert(END,f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.d_ps_p}")
            if self.fanta.get() !=0:
                self.txtarea.insert(END,f"\n Fanta\t\t{self.fanta.get()}\t\t{self.d_f_p}")
            if self.sevnup.get() !=0:
                self.txtarea.insert(END,f"\n 7Up\t\t{self.sevnup.get()}\t\t{self.d_sp_p}")
            if self.marinda.get() !=0:
                self.txtarea.insert(END,f"\n Marinda\t\t{self.marinda.get()}\t\t{self.d_m_p}")

            self.txtarea.insert(END,f"\n -------------------------------------")
            if self.cosmetics_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetics Tax\t\t\t{self.cosmetics_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
            if self.drinks_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Drinks Tax\t\t\t{self.drinks_tax.get()}")

            self.txtarea.insert(END,f"\n Total Bill\t\t\tRs. {str(self.total_bill)}")
            self.txtarea.insert(END,f"\n -------------------------------------")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_data(self):
        op = messagebox.askyesno("Exit", "Do you want to Clear")
        if op>0:

            # Cosmetics
            self.soap.set(0)
            self.face_creame.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)
            # Grocery
            self.rice.set(0)
            self.oil.set(0)
            self.daal.set(0)
            self.floor.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            # Drinks
            self.coke.set(0)
            self.sprite.set(0)
            self.pepsi.set(0)
            self.fanta.set(0)
            self.sevnup.set(0)
            self.marinda.set(0)

            # Total Product Price & Tax Variables
            self.cosmetics_price.set("")
            self.grocery_price.set("")
            self.drinks_price.set("")

            self.cosmetics_tax.set("")
            self.grocery_tax.set("")
            self.drinks_tax.set("")

            # Customers Variable
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit")
        if op>0:
            self.root.destroy()

root = Tk()
obj = Bill_App(root)
root.mainloop()


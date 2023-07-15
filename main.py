from tkinter import *
from tkinter import messagebox

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restoran Sipariş Sistemi")
        self.root.geometry("800x600")  # Uygulama boyutunu ayarla

        # Menü kategorileri ve öğeleri
        self.menu_items = {
            "Yiyecekler": [
                {"name": "Hamburger", "price": 15},
                {"name": "Pizza", "price": 20},
                {"name": "Makarna", "price": 12},
                {"name": "Salata", "price": 8},
                {"name": "Çorba", "price": 6}
            ],
            "İçecekler": [
                {"name": "Kola", "price": 5},
                {"name": "Ayran", "price": 3},
                {"name": "Çay", "price": 2},
                {"name": "Kahve", "price": 4},
                {"name": "Meyve Suyu", "price": 6}
            ],
            "Tatlılar": [
                {"name": "Cheesecake", "price": 10},
                {"name": "Tiramisu", "price": 12},
                {"name": "Muhallebi", "price": 8},
                {"name": "Pasta", "price": 10},
                {"name": "Dondurma", "price": 6}
            ]
        }

        # Alkollü içecekler
        self.menu_items["Alkollü İçecekler"] = [
            {"name": "Bira", "price": 8},
            {"name": "Şarap", "price": 15},
            {"name": "Votka", "price": 10},
            {"name": "Rakı", "price": 12}
        ]

        # Sipariş sepeti
        self.cart = {}

        # Kullanıcı arayüzü elemanları
        self.menu_frame = Frame(root, width=400)
        self.menu_frame.pack(side=LEFT, padx=50, pady=50, fill=Y)

        self.cart_frame = Frame(root)
        self.cart_frame.pack(side=RIGHT, padx=50, pady=50, fill=Y)

        self.checkout_button = Button(self.root, text="Ödemeye Git", command=self.checkout, bg="blue", fg="white")
        self.checkout_button.pack(side=BOTTOM, pady=10)

        self.total_label = Label(self.root, text="Toplam Tutar: $0", font=("Helvetica", 16))
        self.total_label.pack(side=BOTTOM, pady=10, anchor="w")

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.display_menu("Yiyecekler")  # Varsayılan olarak yiyecekler menüsünü görüntüle

    def on_close(self):
        result = messagebox.askquestion("Çıkış", "Uygulamayı kapatmak istediğinize emin misiniz?", icon="warning")
        if result == "yes":
            self.root.destroy()

    def display_menu(self, category):
        # Menüyü temizle
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

        category_label = Label(self.menu_frame, text=category, font=("Helvetica", 16, "bold"))
        category_label.pack(pady=10)

        items = self.menu_items[category]

        for item in items:
            item_frame = Frame(self.menu_frame, bg="white", padx=10, pady=10)
            item_frame.pack(pady=5, fill=X)

            item_label = Label(item_frame, text=item["name"], font=("Helvetica", 12), bg="white")
            item_label.pack(side=LEFT)

            price_label = Label(item_frame, text=f"${item['price']}", font=("Helvetica", 10), bg="white")
            price_label.pack(side=LEFT, padx=10)

            add_button = Button(item_frame, text="Ekle", command=lambda item=item: self.add_to_cart(item), bg="green", fg="white", width=5)
            add_button.pack(side=RIGHT)

    def add_to_cart(self, item):
        name = item["name"]

        if name in self.cart:
            self.cart[name]["quantity"] += 1
        else:
            self.cart[name] = {
                "price": item["price"],
                "quantity": 1
            }

        self.update_cart()

    def remove_from_cart(self, name):
        if name in self.cart:
            if self.cart[name]["quantity"] > 1:
                self.cart[name]["quantity"] -= 1
            else:
                del self.cart[name]

            self.update_cart()

    def update_cart(self):
        for widget in self.cart_frame.winfo_children():
            widget.destroy()

        total_price = 0

        for name, item in self.cart.items():
            item_frame = Frame(self.cart_frame, bg="white", padx=10, pady=10)
            item_frame.pack(pady=5, fill=X)

            item_label = Label(item_frame, text=f"{name} x {item['quantity']}", font=("Helvetica", 12), bg="white")
            item_label.pack(side=LEFT)

            remove_button = Button(item_frame, text="Çıkar", command=lambda name=name: self.remove_from_cart(name), bg="red", fg="white", width=5)
            remove_button.pack(side=RIGHT)

            total_price += item["price"] * item["quantity"]

        self.total_label.config(text=f"Toplam Tutar: ${total_price}")

    def checkout(self):
        if len(self.cart) == 0:
            messagebox.showinfo("Hata", "Sipariş sepeti boş.")
        else:
            messagebox.showinfo("Başarılı", "Siparişiniz alındı. Teşekkür ederiz!")

            self.cart = {}
            self.update_cart()

# Uygulamayı başlat
root = Tk()
app = RestaurantApp(root)

# Yiyecekler butonu
yiyecekler_button = Button(root, text="Yiyecekler", command=lambda: app.display_menu("Yiyecekler"))
yiyecekler_button.pack(side=TOP, pady=10)

# İçecekler butonu
icecekler_button = Button(root, text="İçecekler", command=lambda: app.display_menu("İçecekler"))
icecekler_button.pack(side=TOP, pady=10)

# Tatlılar butonu
tatlilar_button = Button(root, text="Tatlılar", command=lambda: app.display_menu("Tatlılar"))
tatlilar_button.pack(side=TOP, pady=10)

# Alkollü İçecekler butonu
alkollu_icecekler_button = Button(root, text="Alkollü İçecekler", command=lambda: app.display_menu("Alkollü İçecekler"))
alkollu_icecekler_button.pack(side=TOP, pady=10)

root.mainloop()

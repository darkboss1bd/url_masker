import tkinter as tk
from tkinter import messagebox, ttk
import re
import pyperclip

# Main Application
class URLMaskerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔗 DarkBoss1BD - URL Masker Tool")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#0d0d0d")

        # Title Banner
        banner_frame = tk.Frame(root, bg="#00ff00", height=60)
        banner_frame.pack(fill="x")
        banner_label = tk.Label(
            banner_frame,
            text="🛡️ DARKBOSS1BD - URL MASKER TOOL 🛡️",
            font=("Courier", 16, "bold"),
            bg="#00ff00",
            fg="#0d0d0d"
        )
        banner_label.pack(pady=10)

        # Hacker Matrix-like Animation Background
        self.canvas = tk.Canvas(root, bg="#0d0d0d", height=100, highlightthickness=0)
        self.canvas.pack(fill="x")
        self.matrix_chars = "01"
        self.drops = [0] * 100
        self.chars = []
        self.animate_matrix()

        # Main Content
        main_frame = tk.Frame(root, bg="#111")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        tk.Label(main_frame, text="Enter Fake URL (e.g., https://google.com)", 
                 font=("Consolas", 10), fg="#00ff00", bg="#111").pack(anchor="w", padx=10)
        self.fake_url_entry = tk.Entry(main_frame, width=80, font=("Consolas", 10), bg="#222", fg="#00ff00", insertbackground="#00ff00")
        self.fake_url_entry.pack(pady=5)

        tk.Label(main_frame, text="Enter Real URL (to hide, e.g., https://malicious.com)", 
                 font=("Consolas", 10), fg="#00ff00", bg="#111").pack(anchor="w", padx=10)
        self.real_url_entry = tk.Entry(main_frame, width=80, font=("Consolas", 10), bg="#222", fg="#00ff00", insertbackground="#00ff00")
        self.real_url_entry.pack(pady=5)

        # Mask Button
        mask_btn = tk.Button(main_frame, text="🎯 MASK URL", font=("Consolas", 12, "bold"),
                             bg="#00ff00", fg="#0d0d0d", command=self.mask_url, width=20)
        mask_btn.pack(pady=15)

        # Result Area
        tk.Label(main_frame, text="Masked URL (Click to Copy):", 
                 font=("Consolas", 10), fg="#00ff00", bg="#111").pack(anchor="w", padx=10)
        
        self.result_var = tk.StringVar()
        result_entry = tk.Entry(main_frame, textvariable=self.result_var, font=("Consolas", 10),
                                bg="#222", fg="#00ff00", state="readonly", width=80)
        result_entry.pack(pady=5)
        result_entry.bind("<Button-1>", self.copy_url)

        # Footer
        footer = tk.Label(root, text="🔐 Made with ❤️ by darkboss1bd | Educational Purpose Only",
                         font=("Courier", 9), fg="#555", bg="#0d0d0d")
        footer.pack(side="bottom", pady=10)

    def animate_matrix(self):
        self.canvas.delete("all")
        width = 700
        for i in range(len(self.drops)):
            char = self.canvas.create_text(
                i * 10, self.drops[i] * 15,
                text=self.matrix_chars[0], fill="#00ff00", font=("Arial", 10)
            )
            self.chars.append(char)
            if self.drops[i] * 15 > 100 or random.random() > 0.975:
                self.drops[i] = 0
            self.drops[i] += 1
        self.root.after(100, self.animate_matrix)

    def is_valid_url(self, url):
        regex = re.compile(
            r'^(https?://)?'
            r'(([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6})'
            r'(:[0-9]+)?(/.*)?$', re.IGNORECASE)
        return re.match(regex, url) is not None

    def mask_url(self):
        fake_url = self.fake_url_entry.get().strip()
        real_url = self.real_url_entry.get().strip()

        if not fake_url or not real_url:
            messagebox.showwarning("⚠️ Input Error", "Please fill both URLs!")
            return

        if not fake_url.startswith(("http://", "https://")):
            fake_url = "https://" + fake_url
        if not real_url.startswith(("http://", "https://")):
            real_url = "https://" + real_url

        if not self.is_valid_url(fake_url.replace("https://", "").split("@")[0]):
            messagebox.showerror("❌ Invalid Fake URL", "The fake URL domain is not valid!")
            return

        if not self.is_valid_url(real_url):
            messagebox.showerror("❌ Invalid Real URL", "The real URL is not valid!")
            return

        # Masking: fake_url@real_url
        masked_url = f"{fake_url}@{real_url.replace('https://', '').replace('http://', '')}"

        # Final validation
        if len(masked_url) > 2000:
            messagebox.showerror("❌ Too Long", "Masked URL is too long!")
            return

        self.result_var.set(masked_url)
        messagebox.showinfo("✅ Success", "URL Masked Successfully!\nClick on the result to copy.")

    def copy_url(self, event):
        url = self.result_var.get()
        if url:
            pyperclip.copy(url)
            messagebox.showinfo("📋 Copied", "Masked URL copied to clipboard!")


# Run the app
if __name__ == "__main__":
    import random  # For matrix animation
    root = tk.Tk()
    app = URLMaskerApp(root)
    root.mainloop()
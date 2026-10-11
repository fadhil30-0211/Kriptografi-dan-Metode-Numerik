import sys
import random
import numpy as np
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class CryptographyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Cryptography Suite")
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2D2D30;
            }
            QGroupBox {
                background-color: #3E3E40;
                border: 1px solid #007ACC;
                border-radius: 5px;
                margin-top: 1ex;
                color: #DCDCDC;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px 0 3px;
                color: #4EC9B0;
            }
            QTextEdit, QLineEdit {
                background-color: #252526;
                color: #DCDCDC;
                border: 1px solid #3F3F46;
                border-radius: 3px;
                padding: 5px;
            }
            QPushButton {
                background-color: #007ACC;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1C97EA;
            }
            QPushButton:pressed {
                background-color: #005999;
            }
            QLabel {
                color: #DCDCDC;
            }
            QComboBox {
                background-color: #252526;
                color: #DCDCDC;
                border: 1px solid #3F3F46;
                border-radius: 3px;
                padding: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: #252526;
                color: #DCDCDC;
                selection-background-color: #007ACC;
            }
            QTabWidget::pane {
                border: 1px solid #3F3F46;
                background: #2D2D30;
            }
            QTabBar::tab {
                background: #3E3E40;
                color: #DCDCDC;
                padding: 8px 15px;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                border: 1px solid #3F3F46;
            }
            QTabBar::tab:selected {
                background: #007ACC;
                color: white;
            }
        """)
        
        self.init_ui()
        
        # Generate random substitution table
        self.substitution_table = self.generate_substitution_table()
        
    def init_ui(self):
        # Create main tab widget
        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)
        
        # Create tabs for different techniques
        tab_widget.addTab(self.create_substitution_tab(), "Substitusi")
        tab_widget.addTab(self.create_permutation_tab(), "Permutasi")
        tab_widget.addTab(self.create_block_tab(), "Block Cipher")
        tab_widget.addTab(self.create_expansion_tab(), "Ekspansi")
        tab_widget.addTab(self.create_compaction_tab(), "Pemampatan")
        
        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
    def create_substitution_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Technique selection
        technique_group = QGroupBox("Pilih Teknik Substitusi")
        tech_layout = QHBoxLayout()
        self.sub_technique = QComboBox()
        self.sub_technique.addItems(["Tabel Substitusi", "Caesar Cipher", "ROT13", "Vigenère Cipher"])
        tech_layout.addWidget(self.sub_technique)
        technique_group.setLayout(tech_layout)
        
        # Key input
        key_group = QGroupBox("Kunci")
        key_layout = QVBoxLayout()
        self.sub_key = QLineEdit()
        self.sub_key.setPlaceholderText("Masukkan kunci di sini...")
        key_layout.addWidget(self.sub_key)
        key_group.setLayout(key_layout)
        
        # Input area
        input_group = QGroupBox("Input Teks")
        input_layout = QVBoxLayout()
        self.sub_input = QTextEdit()
        self.sub_input.setPlaceholderText("Masukkan plaintext atau ciphertext di sini...")
        input_layout.addWidget(self.sub_input)
        input_group.setLayout(input_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        encrypt_btn = QPushButton("Enkripsi")
        encrypt_btn.clicked.connect(self.encrypt_substitution)
        decrypt_btn = QPushButton("Dekripsi")
        decrypt_btn.clicked.connect(self.decrypt_substitution)
        button_layout.addWidget(encrypt_btn)
        button_layout.addWidget(decrypt_btn)
        
        # Output area
        output_group = QGroupBox("Hasil")
        output_layout = QVBoxLayout()
        self.sub_output = QTextEdit()
        self.sub_output.setReadOnly(True)
        output_layout.addWidget(self.sub_output)
        output_group.setLayout(output_layout)
        
        # Substitution table preview
        table_group = QGroupBox("Tabel Substitusi")
        table_layout = QVBoxLayout()
        self.table_preview = QLabel("Tabel akan ditampilkan setelah dihasilkan")
        self.table_preview.setWordWrap(True)
        table_layout.addWidget(self.table_preview)
        table_group.setLayout(table_layout)
        
        # Add widgets to main layout
        layout.addWidget(technique_group)
        layout.addWidget(key_group)
        layout.addWidget(input_group)
        layout.addLayout(button_layout)
        layout.addWidget(output_group)
        layout.addWidget(table_group)
        
        return tab
    
    def create_permutation_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Technique selection
        technique_group = QGroupBox("Pilih Teknik Permutasi")
        tech_layout = QHBoxLayout()
        self.perm_technique = QComboBox()
        self.perm_technique.addItems(["Kunci Angka", "Zig-zag", "Segitiga", "Spiral", "Diagonal"])
        tech_layout.addWidget(self.perm_technique)
        technique_group.setLayout(tech_layout)
        
        # Key input
        key_group = QGroupBox("Kunci")
        key_layout = QVBoxLayout()
        self.perm_key = QLineEdit()
        self.perm_key.setPlaceholderText("Contoh: 3-1-4-2 untuk permutasi kunci")
        key_layout.addWidget(self.perm_key)
        key_group.setLayout(key_layout)
        
        # Input area
        input_group = QGroupBox("Input Teks")
        input_layout = QVBoxLayout()
        self.perm_input = QTextEdit()
        self.perm_input.setPlaceholderText("Masukkan plaintext atau ciphertext di sini...")
        input_layout.addWidget(self.perm_input)
        input_group.setLayout(input_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        encrypt_btn = QPushButton("Enkripsi")
        encrypt_btn.clicked.connect(self.encrypt_permutation)
        decrypt_btn = QPushButton("Dekripsi")
        decrypt_btn.clicked.connect(self.decrypt_permutation)
        button_layout.addWidget(encrypt_btn)
        button_layout.addWidget(decrypt_btn)
        
        # Output area
        output_group = QGroupBox("Hasil")
        output_layout = QVBoxLayout()
        self.perm_output = QTextEdit()
        self.perm_output.setReadOnly(True)
        output_layout.addWidget(self.perm_output)
        output_group.setLayout(output_layout)
        
        # Visualization area
        viz_group = QGroupBox("Visualisasi Permutasi")
        viz_layout = QVBoxLayout()
        self.perm_viz = QLabel("Visualisasi akan ditampilkan di sini...")
        self.perm_viz.setAlignment(Qt.AlignmentFlag.AlignCenter)
        viz_layout.addWidget(self.perm_viz)
        viz_group.setLayout(viz_layout)
        
        # Add widgets to main layout
        layout.addWidget(technique_group)
        layout.addWidget(key_group)
        layout.addWidget(input_group)
        layout.addLayout(button_layout)
        layout.addWidget(output_group)
        layout.addWidget(viz_group)
        
        return tab
    
    def create_block_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Block size input
        size_group = QGroupBox("Ukuran Blok")
        size_layout = QHBoxLayout()
        self.block_size = QLineEdit()
        self.block_size.setPlaceholderText("Masukkan ukuran blok (contoh: 4)")
        size_layout.addWidget(self.block_size)
        size_group.setLayout(size_layout)
        
        # Input area
        input_group = QGroupBox("Input Teks")
        input_layout = QVBoxLayout()
        self.block_input = QTextEdit()
        self.block_input.setPlaceholderText("Masukkan plaintext atau ciphertext di sini...")
        input_layout.addWidget(self.block_input)
        input_group.setLayout(input_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        encrypt_btn = QPushButton("Enkripsi")
        encrypt_btn.clicked.connect(self.encrypt_block)
        decrypt_btn = QPushButton("Dekripsi")
        decrypt_btn.clicked.connect(self.decrypt_block)
        button_layout.addWidget(encrypt_btn)
        button_layout.addWidget(decrypt_btn)
        
        # Output area
        output_group = QGroupBox("Hasil")
        output_layout = QVBoxLayout()
        self.block_output = QTextEdit()
        self.block_output.setReadOnly(True)
        output_layout.addWidget(self.block_output)
        output_group.setLayout(output_layout)
        
        # Block visualization
        viz_group = QGroupBox("Visualisasi Blok")
        viz_layout = QVBoxLayout()
        self.block_viz = QLabel("Visualisasi blok akan ditampilkan di sini...")
        self.block_viz.setAlignment(Qt.AlignmentFlag.AlignCenter)
        viz_layout.addWidget(self.block_viz)
        viz_group.setLayout(viz_layout)
        
        # Add widgets to main layout
        layout.addWidget(size_group)
        layout.addWidget(input_group)
        layout.addLayout(button_layout)
        layout.addWidget(output_group)
        layout.addWidget(viz_group)
        
        return tab
    
    def create_expansion_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Input area
        input_group = QGroupBox("Input Teks")
        input_layout = QVBoxLayout()
        self.exp_input = QTextEdit()
        self.exp_input.setPlaceholderText("Masukkan plaintext di sini...")
        input_layout.addWidget(self.exp_input)
        input_group.setLayout(input_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        encrypt_btn = QPushButton("Enkripsi")
        encrypt_btn.clicked.connect(self.encrypt_expansion)
        decrypt_btn = QPushButton("Dekripsi")
        decrypt_btn.clicked.connect(self.decrypt_expansion)
        button_layout.addWidget(encrypt_btn)
        button_layout.addWidget(decrypt_btn)
        
        # Output area
        output_group = QGroupBox("Hasil")
        output_layout = QVBoxLayout()
        self.exp_output = QTextEdit()
        self.exp_output.setReadOnly(True)
        output_layout.addWidget(self.exp_output)
        output_group.setLayout(output_layout)
        
        # Rule explanation
        rule_group = QGroupBox("Aturan Ekspansi")
        rule_layout = QVBoxLayout()
        rule_label = QLabel("1. Kata dengan konsonan/angka ganjil di awal: pindahkan ke akhir + 'an'\n"
                           "2. Kata dengan vokal/angka genap di awal: tambahkan 'i' di akhir\n"
                           "Contoh: 'Ulang' -> 'Languan', 'Tahun' -> 'Ahunti'")
        rule_label.setWordWrap(True)
        rule_layout.addWidget(rule_label)
        rule_group.setLayout(rule_layout)
        
        # Add widgets to main layout
        layout.addWidget(input_group)
        layout.addLayout(button_layout)
        layout.addWidget(output_group)
        layout.addWidget(rule_group)
        
        return tab
    
    def create_compaction_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Input area
        input_group = QGroupBox("Input Teks")
        input_layout = QVBoxLayout()
        self.comp_input = QTextEdit()
        self.comp_input.setPlaceholderText("Masukkan plaintext di sini...")
        input_layout.addWidget(self.comp_input)
        input_group.setLayout(input_layout)
        
        # Buttons
        button_layout = QHBoxLayout()
        encrypt_btn = QPushButton("Enkripsi")
        encrypt_btn.clicked.connect(self.encrypt_compaction)
        decrypt_btn = QPushButton("Dekripsi")
        decrypt_btn.clicked.connect(self.decrypt_compaction)
        button_layout.addWidget(encrypt_btn)
        button_layout.addWidget(decrypt_btn)
        
        # Output area
        output_group = QGroupBox("Hasil")
        output_layout = QVBoxLayout()
        self.comp_output = QTextEdit()
        self.comp_output.setReadOnly(True)
        output_layout.addWidget(self.comp_output)
        output_group.setLayout(output_layout)
        
        # Rule explanation
        rule_group = QGroupBox("Aturan Pemampatan")
        rule_layout = QVBoxLayout()
        rule_label = QLabel("1. Hilangkan setiap karakter ke-3 secara berurutan\n"
                           "2. Karakter yang dihilangkan disatukan sebagai lampiran\n"
                           "3. Pisahkan lampiran dengan karakter '&'\n"
                           "Contoh: 'KRIPTOGRAFI' -> 'KIPOGFI&RTRA'")
        rule_label.setWordWrap(True)
        rule_layout.addWidget(rule_label)
        rule_group.setLayout(rule_layout)
        
        # Add widgets to main layout
        layout.addWidget(input_group)
        layout.addLayout(button_layout)
        layout.addWidget(output_group)
        layout.addWidget(rule_group)
        
        return tab
    
    # =====================
    # SUBSTITUTION METHODS
    # =====================
    def generate_substitution_table(self):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?"
        shuffled = list(chars)
        random.shuffle(shuffled)
        return dict(zip(chars, shuffled))
    
    def encrypt_substitution(self):
        technique = self.sub_technique.currentText()
        text = self.sub_input.toPlainText()
        
        if not text:
            self.status_bar.showMessage("Input teks kosong!", 3000)
            return
        
        if technique == "Tabel Substitusi":
            result = ''.join(self.substitution_table.get(c, c) for c in text)
            # Update table preview
            table_text = "Tabel Substitusi:\n"
            for k, v in self.substitution_table.items():
                table_text += f"{k} → {v}  "
                if k in "M13?":
                    table_text += "\n"
            self.table_preview.setText(table_text)
            
        elif technique == "Caesar Cipher":
            key = self.sub_key.text().strip()
            shift = 3 if not key else int(key) % 26
            result = self.caesar_cipher(text, shift)
            
        elif technique == "ROT13":
            result = self.caesar_cipher(text, 13)
            
        elif technique == "Vigenère Cipher":
            key = self.sub_key.text().strip()
            if not key:
                self.status_bar.showMessage("Kunci diperlukan untuk Vigenère!", 3000)
                return
            result = self.vigenere_cipher(text, key, encrypt=True)
            
        self.sub_output.setText(result)
        self.status_bar.showMessage(f"Enkripsi {technique} berhasil!", 3000)
    
    def decrypt_substitution(self):
        technique = self.sub_technique.currentText()
        text = self.sub_input.toPlainText()
        
        if not text:
            self.status_bar.showMessage("Input teks kosong!", 3000)
            return
        
        if technique == "Tabel Substitusi":
            reverse_table = {v: k for k, v in self.substitution_table.items()}
            result = ''.join(reverse_table.get(c, c) for c in text)
            
        elif technique == "Caesar Cipher":
            key = self.sub_key.text().strip()
            shift = 3 if not key else int(key) % 26
            result = self.caesar_cipher(text, -shift)
            
        elif technique == "ROT13":
            result = self.caesar_cipher(text, -13)
            
        elif technique == "Vigenère Cipher":
            key = self.sub_key.text().strip()
            if not key:
                self.status_bar.showMessage("Kunci diperlukan untuk Vigenère!", 3000)
                return
            result = self.vigenere_cipher(text, key, encrypt=False)
            
        self.sub_output.setText(result)
        self.status_bar.showMessage(f"Dekripsi {technique} berhasil!", 3000)
    
    def caesar_cipher(self, text, shift):
        result = []
        for char in text:
            if char.isupper():
                base = ord('A')
                result.append(chr((ord(char) - base + shift) % 26 + base))
            elif char.islower():
                base = ord('a')
                result.append(chr((ord(char) - base + shift) % 26 + base))
            else:
                result.append(char)
        return ''.join(result)
    
    def vigenere_cipher(self, text, key, encrypt=True):
        key = key.upper()
        key_length = len(key)
        result = []
        key_idx = 0
        
        for char in text:
            if char.isalpha():
                shift = ord(key[key_idx % key_length]) - ord('A')
                if not encrypt:
                    shift = -shift
                
                if char.isupper():
                    base = ord('A')
                    result.append(chr((ord(char) - base + shift) % 26 + base))
                else:
                    base = ord('a')
                    result.append(chr((ord(char) - base + shift) % 26 + base))
                
                key_idx += 1
            else:
                result.append(char)
        
        return ''.join(result)
    
    # =====================
    # PERMUTATION METHODS
    # =====================
    def encrypt_permutation(self):
        technique = self.perm_technique.currentText()
        text = self.perm_input.toPlainText()
        
        if not text:
            self.status_bar.showMessage("Input teks kosong!", 3000)
            return
        
        if technique == "Kunci Angka":
            key_str = self.perm_key.text().strip()
            if not key_str:
                self.status_bar.showMessage("Kunci diperlukan untuk permutasi angka!", 3000)
                return
            try:
                key = [int(k) for k in key_str.split('-')]
                result, viz = self.key_permutation(text, key, encrypt=True)
            except ValueError:
                self.status_bar.showMessage("Format kunci tidak valid! Gunakan format seperti 3-1-4-2", 3000)
                return
            
        elif technique == "Zig-zag":
            result, viz = self.zigzag_permutation(text, encrypt=True)
            
        elif technique == "Segitiga":
            result, viz = self.triangle_permutation(text, encrypt=True)
            
        elif technique == "Spiral":
            result, viz = self.spiral_permutation(text, encrypt=True)
            
        elif technique == "Diagonal":
            result, viz = self.diagonal_permutation(text, encrypt=True)
            
        self.perm_output.setText(result)
        self.perm_viz.setText(viz)
        self.status_bar.showMessage(f"Enkripsi {technique} berhasil!", 3000)
    
    def decrypt_permutation(self):
        technique = self.perm_technique.currentText()
        text = self.perm_input.toPlainText()
        
        if not text:
            self.status_bar.showMessage("Input teks kosong!", 3000)
            return
        
        if technique == "Kunci Angka":
            key_str = self.perm_key.text().strip()
            if not key_str:
                self.status_bar.showMessage("Kunci diperlukan untuk permutasi angka!", 3000)
                return
            try:
                key = [int(k) for k in key_str.split('-')]
                result, viz = self.key_permutation(text, key, encrypt=False)
            except ValueError:
                self.status_bar.showMessage("Format kunci tidak valid! Gunakan format seperti 3-1-4-2", 3000)
                return
            
        elif technique == "Zig-zag":
            result, viz = self.zigzag_permutation(text, encrypt=False)
            
        elif technique == "Segitiga":
            result, viz = self.triangle_permutation(text, encrypt=False)
            
        elif technique == "Spiral":
            result, viz = self.spiral_permutation(text, encrypt=False)
            
        elif technique == "Diagonal":
            result, viz = self.diagonal_permutation(text, encrypt=False)
            
        self.perm_output.setText(result)
        self.perm_viz.setText(viz)
        self.status_bar.showMessage(f"Dekripsi {technique} berhasil!", 3000)
    
    def key_permutation(self, text, key, encrypt=True):
        n = len(key)
        # Add padding if needed
        padding = (n - len(text) % n) % n
        text += 'X' * padding
        
        if encrypt:
            # Split text into chunks
            chunks = [text[i:i+n] for i in range(0, len(text), n)]
            result = []
            viz = "Permutasi dengan Kunci:\n"
            
            for chunk in chunks:
                viz += f"Plain:  {' '.join(chunk)}\n"
                permuted = ''.join(chunk[i-1] for i in key)
                viz += f"Cipher: {' '.join(permuted)}\n\n"
                result.append(permuted)
            
            return ''.join(result), viz
        else:
            # Create inverse key
            inverse_key = [0] * len(key)
            for i, k in enumerate(key):
                inverse_key[k-1] = i+1
            
            chunks = [text[i:i+n] for i in range(0, len(text), n)]
            result = []
            viz = "Inverse Permutasi dengan Kunci:\n"
            
            for chunk in chunks:
                viz += f"Cipher: {' '.join(chunk)}\n"
                original = ''.join(chunk[inverse_key[i]-1] for i in range(len(key)))
                viz += f"Plain:  {' '.join(original)}\n\n"
                result.append(original)
            
            return ''.join(result).rstrip('X'), viz
    
    def zigzag_permutation(self, text, encrypt=True):
        n = 4  # Fixed row size for simplicity
        # Calculate column size
        cols = (len(text) + n - 1) // n
        # Add padding if needed
        padding = (cols * n) - len(text)
        text += 'X' * padding
        
        if encrypt:
            # Create matrix
            matrix = [list(text[i*cols:(i+1)*cols]) for i in range(n)]
            
            # Build visualization
            viz = "Zig-zag Permutation:\n"
            for row in matrix:
                viz += ' '.join(row) + '\n'
            viz += "\nCiphertext: "
            
            # Read in zig-zag pattern
            result = []
            for col in range(cols):
                if col % 2 == 0:  # Top to bottom
                    for row in range(n):
                        result.append(matrix[row][col])
                else:  # Bottom to top
                    for row in range(n-1, -1, -1):
                        result.append(matrix[row][col])
            
            viz += ''.join(result)
            return ''.join(result), viz
        else:
            # Invert the process
            result = [''] * len(text)
            idx = 0
            
            for col in range(cols):
                if col % 2 == 0:
                    for row in range(n):
                        result[row*cols + col] = text[idx]
                        idx += 1
                else:
                    for row in range(n-1, -1, -1):
                        result[row*cols + col] = text[idx]
                        idx += 1
            
            viz = "Inverse Zig-zag:\nCiphertext: " + text + "\nPlaintext: " + ''.join(result).rstrip('X')
            return ''.join(result).rstrip('X'), viz
    
    def triangle_permutation(self, text, encrypt=True):
        # This is a simplified implementation
        if encrypt:
            # Alternate between first and last characters
            result = []
            viz = "Triangle Permutation:\nPlain: " + text + "\n"
            left, right = [], []
            for i, char in enumerate(text):
                if i % 2 == 0:
                    left.append(char)
                else:
                    right.insert(0, char)
            result = ''.join(left + right)
            viz += "Cipher: " + result
            return result, viz
        else:
            # Invert the process
            n = len(text)
            mid = (n + 1) // 2
            left = list(text[:mid])
            right = list(text[mid:])[::-1]
            
            result = []
            for i in range(max(len(left), len(right))):
                if i < len(left):
                    result.append(left[i])
                if i < len(right):
                    result.append(right[i])
            
            viz = "Inverse Triangle:\nCipher: " + text + "\nPlain: " + ''.join(result)
            return ''.join(result), viz
    
    def spiral_permutation(self, text, encrypt=True):
        # This is a placeholder implementation
        if encrypt:
            # Simple reverse for demonstration
            result = text[::-1]
            viz = f"Spiral Permutation:\nPlain: {text}\nCipher: {result}"
            return result, viz
        else:
            result = text[::-1]
            viz = f"Inverse Spiral:\nCipher: {text}\nPlain: {result}"
            return result, viz
    
    def diagonal_permutation(self, text, encrypt=True):
        # This is a placeholder implementation
        if encrypt:
            # Swap adjacent characters
            chars = list(text)
            for i in range(0, len(chars)-1, 2):
                chars[i], chars[i+1] = chars[i+1], chars[i]
            result = ''.join(chars)
            viz = f"Diagonal Permutation:\nPlain: {text}\nCipher: {result}"
            return result, viz
        else:
            chars = list(text)
            for i in range(0, len(chars)-1, 2):
                chars[i], chars[i+1] = chars[i+1], chars[i]
            result = ''.join(chars)
            viz = f"Inverse Diagonal:\nCipher: {text}\nPlain: {result}"
            return result, viz
    
    # =================
    # BLOCK CIPHER
    # =================
    def encrypt_block(self):
        text = self.block_input.toPlainText().replace(" ", "")
        size_str = self.block_size.text().strip()
        
        if not text:
            self.status_bar.showMessage("Input teks kosong!", 3000)
            return
        
        if not size_str:
            self.status_bar.showMessage("Ukuran blok diperlukan!", 3000)
            return
        
        try:
            size = int(size_str)
        except ValueError:
            self.status_bar.showMessage("Ukuran blok harus berupa angka!", 3000)
            return
        
        # Add padding if needed
        padding = (size - len(text) % size)
        if padding > 0:
            text += 'X' * padding
        
        # Create blocks
        blocks = [text[i:i+size] for i in range(0, len(text), size)]
        
        # Build visualization
        viz = "Blok Plaintext:\n"
        for i, block in enumerate(blocks):
            viz += f"Blok {i+1}: {' '.join(block)}\n"
        
        # Transpose blocks
        cipher_blocks = []
        for block in blocks:
            # Write vertically, read horizontally
            cols = min(size, len(block))
            rows = (len(block) + cols - 1) // cols
            matrix = [list(block[i*cols:(i+1)*cols]) for i in range(rows)]
            
            # If matrix is incomplete, fill with placeholder
            if len(matrix[-1]) < cols:
                matrix[-1] += ['X'] * (cols - len(matrix[-1]))
            
            # Read horizontally
            transposed = []
            for c in range(cols):
                for r in range(rows):
                    transposed.append(matrix[r][c])
            cipher_blocks.append(''.join(transposed))
        
        result = ''.join(cipher_blocks)
        viz += "\nBlok Ciphertext:\n"
        for i, block in enumerate(cipher_blocks):
            viz += f"Blok {i+1}: {' '.join(block)}\n"
        
        self.block_output.setText(result)
        self.block_viz.setText(viz)
        self.status_bar.showMessage("Enkripsi Block Cipher berhasil!", 3000)
    
    def decrypt_block(self):
        text = self.block_input.toPlainText().replace(" ", "")
        size_str = self.block_size.text().strip()
        
        if not text:
            self.status_bar.showMessage("Input teks kosong!", 3000)
            return
        
        if not size_str:
            self.status_bar.showMessage("Ukuran blok diperlukan!", 3000)
            return
        
        try:
            size = int(size_str)
        except ValueError:
            self.status_bar.showMessage("Ukuran blok harus berupa angka!", 3000)
            return
        
        # Create blocks
        blocks = [text[i:i+size] for i in range(0, len(text), size)]
        
        # Build visualization
        viz = "Blok Ciphertext:\n"
        for i, block in enumerate(blocks):
            viz += f"Blok {i+1}: {' '.join(block)}\n"
        
        # Inverse transpose
        plain_blocks = []
        for block in blocks:
            # Write horizontally, read vertically
            rows = min(size, len(block))  # Transpose reverses rows/cols
            cols = (len(block) + rows - 1) // rows
            matrix = [list(block[i*cols:(i+1)*cols]) for i in range(rows)]
            
            # If matrix is incomplete, fill with placeholder
            if len(matrix[-1]) < cols:
                matrix[-1] += ['X'] * (cols - len(matrix[-1]))
            
            # Read vertically
            original = []
            for c in range(cols):
                for r in range(rows):
                    original.append(matrix[r][c])
            plain_blocks.append(''.join(original))
        
        result = ''.join(plain_blocks).rstrip('X')
        viz += "\nBlok Plaintext:\n"
        for i, block in enumerate(plain_blocks):
            viz += f"Blok {i+1}: {' '.join(block)}\n"
        
        self.block_output.setText(result)
        self.block_viz.setText(viz)
        self.status_bar.showMessage("Dekripsi Block Cipher berhasil!", 3000)
    
    # =================
    # EXPANSION CIPHER
    # =================
    def encrypt_expansion(self):
        text = self.exp_input.toPlainText()
        
        if not text:
            self.status_bar.showMessage("Input teks kosong!", 3000)
            return
        
        # Split into words
        words = text.split()
        result = []
        
        for word in words:
            # Remove non-alphanumeric characters
            clean_word = ''.join(filter(str.isalnum, word))
            if not clean_word:
                result.append(word)
                continue
            
            # Check first character
            first_char = clean_word[0]
            if first_char.isdigit():
                num = int(first_char)
                if num % 2 == 1:  # Odd number
                    transformed = clean_word[1:] + first_char + "an"
                else:  # Even number
                    transformed = clean_word + "i"
            elif first_char.lower() in 'aeiou':  # Vowel
                transformed = clean_word + "i"
            else:  # Consonant
                transformed = clean_word[1:] + first_char + "an"
            
            # Preserve original non-alphanumeric characters
            if word != clean_word:
                transformed = word.replace(clean_word, transformed)
            
            result.append(transformed)
        
        self.exp_output.setText(' '.join(result))
        self.status_bar.showMessage("Enkripsi Ekspansi berhasil!", 3000)
    
    def decrypt_expansion(self):
        text = self.exp_input.toPlainText()
        
        if not text:
            self.status_bar.showMessage("Input teks kosong!", 3000)
            return
        
        # Split into words
        words = text.split()
        result = []
        
        for word in words:
            # Remove non-alphanumeric characters
            clean_word = ''.join(filter(str.isalnum, word))
            if not clean_word:
                result.append(word)
                continue
            
            # Check for patterns
            if clean_word.endswith("an") and len(clean_word) > 3:
                # Check if it's a consonant pattern
                if not clean_word[-3] in 'aeiouAEIOU':
                    original = clean_word[-3] + clean_word[:-3]
                    result.append(word.replace(clean_word, original))
                    continue
            elif clean_word.endswith("i") and len(clean_word) > 1:
                # Check if it's a vowel pattern
                if clean_word[-2] in 'aeiouAEIOU':
                    original = clean_word[:-1]
                    result.append(word.replace(clean_word, original))
                    continue
            
            # If no pattern matched, return original
            result.append(word)
        
        self.exp_output.setText(' '.join(result))
        self.status_bar.showMessage("Dekripsi Ekspansi berhasil!", 3000)
    
    # ===================
    # COMPACTION CIPHER
    # ===================
    def encrypt_compaction(self):
        text = self.comp_input.toPlainText()
        
        if not text:
            self.status_bar.showMessage("Input teks kosong!", 3000)
            return
        
        # Remove spaces for compaction
        clean_text = text.replace(" ", "")
        main_text = []
        removed_chars = []
        
        # Process every 3rd character
        for i, char in enumerate(clean_text):
            if (i + 1) % 3 == 0:  # Every 3rd character
                removed_chars.append(char)
            else:
                main_text.append(char)
        
        # Combine results
        result = ''.join(main_text) + '&' + ''.join(removed_chars)
        self.comp_output.setText(result)
        self.status_bar.showMessage("Enkripsi Pemampatan berhasil!", 3000)
    
    def decrypt_compaction(self):
        text = self.comp_input.toPlainText()
        
        if not text:
            self.status_bar.showMessage("Input teks kosong!", 3000)
            return
        
        # Split main text and removed characters
        if '&' in text:
            main_part, removed_part = text.split('&', 1)
        else:
            main_part = text
            removed_part = ""
        
        # Reconstruct original text
        result = []
        removed_idx = 0
        
        # Calculate positions for insertion
        for i in range(len(main_part) + len(removed_part)):
            if (i + 1) % 3 == 0 and removed_idx < len(removed_part):
                result.append(removed_part[removed_idx])
                removed_idx += 1
            else:
                if main_part:
                    result.append(main_part[0])
                    main_part = main_part[1:]
        
        # Add any remaining characters
        result.extend(list(main_part))
        
        self.comp_output.setText(''.join(result))
        self.status_bar.showMessage("Dekripsi Pemampatan berhasil!", 3000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptographyApp()
    window.show()
    sys.exit(app.exec())
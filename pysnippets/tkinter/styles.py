from tkinter import ttk

def configure_styles():
    """
    Configures and applies custom styles to ttk widgets.
    """
    style = ttk.Style()
    
    # Set the theme to 'clam' which is more customizable
    style.theme_use('clam')
    
    # Configure a style for TButton
    style.configure('Custom.TButton',
                    foreground='white',
                    background='#4CAF50',
                    font=('Helvetica', 12, 'bold'))
    
    style.map('Custom.TButton',
              background=[('active', '#45a049')])
    
    # Configure a style for TLabel
    style.configure('Custom.TLabel',
                    foreground='#333333',
                    font=('Helvetica', 10))
    
    # Configure a style for TEntry
    style.configure('Custom.TEntry',
                    foreground='#000000',
                    font=('Helvetica', 10)) 
from nicegui import ui, app

def create():
    @ui.page('/')
    def page():
        # Initialize counter value in user storage to persist across page reloads
        if 'counter' not in app.storage.user:
            app.storage.user['counter'] = 0
        
        # Create the counter display
        counter_label = ui.label().classes('text-6xl font-bold text-center mb-8').mark('counter-display')
        
        def update_counter_display():
            counter_label.set_text(str(app.storage.user['counter']))
        
        def increment():
            app.storage.user['counter'] += 1
            update_counter_display()
        
        def decrement():
            app.storage.user['counter'] -= 1
            update_counter_display()
        
        # Layout the UI
        with ui.column().classes('items-center justify-center min-h-screen gap-4'):
            counter_label
            
            with ui.row().classes('gap-4'):
                ui.button('-', on_click=decrement).classes('text-2xl px-6 py-3').mark('decrement-btn')
                ui.button('+', on_click=increment).classes('text-2xl px-6 py-3').mark('increment-btn')
        
        # Set initial display
        update_counter_display()
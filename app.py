import interface_image_display
import interface_settings


if __name__ == "__main__":
    app = interface_image_display.create_app()
    settings_frame = interface_settings.add_settings()
    app.mainloop()
    

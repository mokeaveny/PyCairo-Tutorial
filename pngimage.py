import cairo

# Create a function called main
def main():
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, 390, 60)
    cr = cairo.Context(ims)

    cr.set_source_rgb(0, 0, 0)
    cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
        cairo.FONT_WEIGHT_NORMAL)
    cr.set_font_size(40)

    cr.move_to(10, 50)
    cr.show_text("Dizziplin ist Macht.")

    ims.write_to_png("image.png")

if __name__ == "__main__":
    main()
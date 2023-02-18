# For QRCode spec, see the link below:
# https://www.qrcode.com/en/about/standards.html
import qrcode
import gradio as gr

def url_to_qrcode(url, box_size, version):
    q = qrcode.QRCode(
            version = version, # QRCode 的方塊數
            error_correction=qrcode.ERROR_CORRECT_H,
            box_size=box_size, # 單一方塊的邊長點數
            border=20
            )
    q.add_data(url)
    q.make()
    img = q.make_image()
    img.save("qrcode.png")
    return "qrcode.png"

ui = gr.Interface(
        fn=url_to_qrcode,
        inputs=[
            gr.Text(
                label="請輸入 URL："
                ),
            gr.Slider(
                label="QRcode 方塊單邊點數：",
                minimum=2,
                maximum=100,
                value=4,
                step=1
                ),
            gr.Slider(
                label="Version：",
                minimum=1,
                maximum=40,
                value=1,
                step=1
                )
            ],
        outputs=gr.Image(
            type="filepath",
            label=""
            )
        )
ui.launch()


from ultralytics import YOLO #YOLO套件
import cv2 #影像處理工具

model = YOLO("yolov8n.pt")
# results = model("https://ultralytics.com/images/bus.jpg")

# # 找出 YOLO 類別名稱中 'person' 的 ID
# person_id = [k for k, v in model.names.items() if v == "person"][0]

# # 過濾只保留類別是 person 的 box
# boxes = results[0].boxes
# filtered = boxes.cls == person_id
# results[0].boxes = boxes[filtered]

# # 顯示結果
# results[0].show()



# 開啟影片檔案
cap = cv2.VideoCapture("images/video.mp4")

# 取得影片的寬度、高度、每秒幾幀 (fps)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# 每一幀進行偵測與輸出
while cap.isOpened():
    ret, frame = cap.read()  # 讀取一幀
    if not ret:
        break  # 如果讀不到就跳出

    results = model(frame)            # 使用 YOLO 模型做物件偵測
    annotated_frame = results[0].plot()  # 畫出偵測結果（加框和標籤）

    out.write(annotated_frame)  # 寫入輸出影片

# 釋放資源
cap.release()
out.release()


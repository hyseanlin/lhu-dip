import numpy as np
import cv2

# 全域變數來儲存滑鼠點擊的座標
start_point = None
end_point = None
cropping = False

def mergeROIs(roi):
    roi_r = np.zeros_like(roi)
    roi_g = np.zeros_like(roi)
    roi_b = np.zeros_like(roi)

    roi_r [:, :, 2] = roi[:, :, 2]
    roi_g [:, :, 1] = roi[:, :, 1]
    roi_b [:, :, 0] = roi[:, :, 0]

    upper_img = np.concatenate((roi, roi_r), axis=1)
    lower_img = np.concatenate((roi_g, roi_b), axis=1)
    merged_img = np.concatenate((upper_img, lower_img), axis=0)
    
    return merged_img


def mouse_crop(event, x, y, flags, param):
    """
    處理滑鼠事件的函數。
    """
    global start_point, end_point, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        # 滑鼠左鍵按下，記錄起點座標
        start_point = (x, y)
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE and cropping:
        # 當滑鼠移動且處於選取狀態時，更新終點座標
        end_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        # 滑鼠左鍵釋放，記錄終點座標並完成裁剪
        end_point = (x, y)
        cropping = False

def select_roi_without_selectROI(image_path):
    """
    使用滑鼠事件實現感興趣區域（ROI）選取功能。
    """
    global start_point, end_point

    # 讀取圖像
    image = cv2.imread(image_path)
    if image is None:
        print("無法讀取圖片，請檢查路徑！")
        return

    clone = image.copy()
    cv2.namedWindow("Image") #, cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Image", mouse_crop)

    print("請透過滑鼠選取感興趣區域：左鍵按下為起點，拖曳並鬆開為終點。按 'r' 重置選取，或按 'c' 確認選取。")

    while True:
        temp_image = clone.copy()

        # 如果有選取區域，顯示矩形框
        if start_point and end_point and cropping:
            cv2.rectangle(temp_image, start_point, end_point, (0, 255, 0), 2)

        cv2.imshow("Image", temp_image)

        key = cv2.waitKey(1) & 0xFF

        # 按 'r' 重置選取
        if key == ord("r"):
            start_point = None
            end_point = None
            clone = image.copy()

        # 按 'c' 確認選取
        elif key == ord("c"):
            if start_point and end_point:
                x1, y1 = start_point
                x2, y2 = end_point
                roi = clone[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
                
                roi_merged = mergeROIs(roi)

                # 顯示選取的區域
                cv2.imshow("Selected ROI", roi_merged)
                cv2.imwrite("selected_roi.jpg", roi_merged)  # 保存選取區域
                print("已保存選取區域為 'selected_roi.jpg'。")
                cv2.waitKey(0)
            break

        # 按 'q' 退出
        elif key == ord("q"):
            print("退出未保存任何選取區域。")
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 指定圖片的路徑
    image_path = input("請輸入圖片路徑：")
    select_roi_without_selectROI(image_path)

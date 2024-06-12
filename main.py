import threading
from vision.vision2 import *
from motor.motor3 import *
from motor.control import *
from motor.control import move_x, move_y
# from vision.vision2 import center_x, center_y, obj_center_x, obj_center_y, x1, y1, x2, y2
from motor.key import wait_for_key
from motor.shot import *
# from vision.state import state

# torch.set_num_threads(1)a
# os.environ["OMP_NUM_THREADS"] = "1"




capture_thread = threading.Thread(target=capture_and_display, args=(capture_cpu_cores,))
process_thread = threading.Thread(target=process_frame, args=(process_cpu_cores,))
key_thread = threading.Thread(target=wait_for_key)
# move_xth = threading.Thread(target=move_x(state.center_x, state.center_y, state.obj_center_x, state.obj_center_y, state.x1, state.y1, state.x2, state.y2))
# move_yth = threading.Thread(target=move_y(state.center_x, state.center_y, state.obj_center_x, state.obj_center_y, state.x1, state.y1, state.x2, state.y2))
move_xth = threading.Thread(target=move_x)
move_yth = threading.Thread(target=move_y)

           

capture_thread.start()
process_thread.start()
key_thread.start()
move_xth.start()
move_yth.start()

capture_thread.join()
process_thread.join()
key_thread.join()
move_xth.join()
move_yth.join()



# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()

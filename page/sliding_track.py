import numpy as np
from selenium.webdriver.common.action_chains import ActionChains


def ease_out_quad(x):
    return 1 - (1 - x) * (1 - x)


def ease_out_quart(x):
    return 1 - pow(1 - x, 4)


def ease_out_expo(x):
    if x == 1:
        return 1
    else:
        return 1 - pow(2, -10 * x)


def get_tracks(distance, seconds):
    """
    :param distance: offset
    :param seconds: 拉动时间
    :return:
    """
    tracks = [0]
    offsets = [0]
    # print("np_value:", np.arange(0.0, seconds, 0.1))
    for t in np.arange(0.0, seconds, 0.1):
        offset = round(ease_out_quart(t / seconds) * distance)
        tracks.append(offset - offsets[-1])
        offsets.append(offset)
    return offsets, tracks


def drag_and_drop(browser, offset, knob):
    """
    拖拽
    :param browser: 浏览器对象
    :param offset: 滑块到缺口的距离
    :param knob: 滑块的位置
    """
    offsets, tracks = get_tracks(offset, 12)
    # print("offsets:", offsets)
    # print("tracks:", tracks)
    ActionChains(browser).click_and_hold(knob).perform()
    for x in tracks:
        ActionChains(browser).move_by_offset(x, 0).perform()

    ActionChains(browser).pause(0.5).release().perform()
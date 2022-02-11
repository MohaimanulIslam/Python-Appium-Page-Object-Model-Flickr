from selenium.webdriver.common.by import By


class SignInPageLocators(object):
    GET_STARTED = (By.ID, "com.flickr.android:id/activity_welcome_sign_button")
    ENTER_EMAIL = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                             ".FrameLayout" \
                             "/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android"
                             ".webkit" \
                             ".WebView/android.view.View/android.view.View/android.view.View/android.view.View"
                             "/android.view" \
                             ".View[2]/android.view.View/android.view.View/android.widget.EditText ")
    NEXT_BTN = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                          ".FrameLayout/android" \
                          ".widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit"
                          ".WebView/android" \
                          ".view.View/android.view.View/android.view.View/android.view.View/android.view.View[" \
                          "2]/android.widget.Button ")
    ENTER_PASS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                            ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit"
                            ".WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View"
                            "/android.view.View/android.view.View[2]/android.view.View["
                            "2]/android.view.View/android.widget.EditText ")
    SIGN_IN_BTN = (
        By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                  "/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit" \
                  ".WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view" \
                  ".View[2]/android.widget.Button ")

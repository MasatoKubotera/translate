# 

---
## Overview

Using googletrans, I created a ROS package that translates from Japanese to various languages.

(googletransを用いて、日本語から様々な言語に翻訳するROSパッケージを作成しました。)

---
## Movie

[![デモ動画](https://img.youtube.com/vi//maxresdefault.jpg)]()

Click the image to jump to Youtube.

(画像をクリックするとYoutubeに飛びます.)

---
## Version
-   ubuntu
    -   20.04.1 LTS

-   ROS
    -   Noetic

-   googletrans
    -   4.0.0-rc1

-   Python
    -   3.8.5

---
## Build Environment
-   ### ROS
    It has built ROS environment using the following script.

    (下記のスクリプトを使用しROS環境を構築しました。)

    [ros_setup_scripts_Ubuntu20.04_desktop](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop)

-   ### Workspace

    It has created a workspace by referring to the following document.

    (下記の資料を参考にワークスペースを作成しました。)

    [robosys2020](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)

-   ### Package

    Run the following command to clone the package.

    (下記のコマンドを実行し、パッケージをクローンしてください。)

    ```
    $ cd ~/catkin_ws/src
    $ git clone https://github.com/MasatoKubotera/translate
    ```

-   ### Googletrans
    -   Install

        Run the following command to install googletrans.

        (下記のコマンドを実行し、googletransをインストールしてください。)

        ```
        $ pip3 install googletrans==4.0.0-rc1
        ```

    -   Version confirmation

        ```
        $ pip3 list | grep googletrans
        googletrans                   4.0.0rc1
        ```

    -   Sample code

        After installation, run the sample program and check that "こんにちは" is output.

        (インストール後、サンプルプログラムを実行して、"こんにちは"と出力されることを確認してください。)

        ```
        $ cd ~/catkin_ws/src/translate/scripts
        $ python3 translate-test.py
        こんにちは
        ```
---
## Run

-   ### Method - 1

    First of all, please launch the roscore running `$ roscore`.

    (まずはじめに、`$roscore`を実行してroscoreを立ち上げてください。)

    Run the publisher and each subscriber on different window(terminals).

    (パブリッシャ・サブスクライバをそれぞれ別のウィンド(端末)でコマンドを実行してください。)


    -   Publisher

        |Node Name|Code|Run Command|Explanation|
        |---|---|---|---|
        |master_ja|[ja.py](https://github.com/MasatoKubotera/translate/blob/master/scripts/ja.py)|`$ rosrun translate ja.py`|日本語の文字列をサブスクライバに送信|

    -   Subscriber

        Translate the Japanese character string received from the publisher into each language.

        (パブリッシャから受け取った日本語の文字列をそれぞれの言語に翻訳します。)

        |Node Name|Code|Run Command|Description(説明)|
        |---|---|---|---|
        |translate_en|[en.py](https://github.com/MasatoKubotera/translate/blob/master/scripts/en.py)|`$ rosrun translate en.py`|Translate to english(英語に翻訳)|
        |translate_de|[de.py](https://github.com/MasatoKubotera/translate/blob/master/scripts/de.py)|`$ rosrun translate de.py`|Translate to german(ドイツ語に翻訳)|
        |translate_es|[es.py](https://github.com/MasatoKubotera/translate/blob/master/scripts/es.py)|`$ rosrun translate es.py`|Translate to spanish(スペイン語に翻訳)|
        |translate_fr|[fr.py](https://github.com/MasatoKubotera/translate/blob/master/scripts/fr.py)|`$ rosrun translate fr.py`|Translate to french(フランス語に翻訳)|
        |translate_zh|[zh.py](https://github.com/MasatoKubotera/translate/blob/master/scripts/zh.py)|`$ rosrun translate zh.py`|Translate to chinese(中国語(簡体字)に翻訳)|
        |translate_ko|[ko.py](https://github.com/MasatoKubotera/translate/blob/master/scripts/ko.py)|`$ rosrun translate ko.py`|Translate to chinese(韓国語に翻訳)|
        |translate_random|[random_lang.py](https://github.com/MasatoKubotera/translate/blob/master/scripts/random_lang.py)|`$ rosrun translate random.py`|Translate to random language(ランダムな言語に翻訳)|

-   ### Method - 2
    You can launch roscore, publisher, and all subscribers by running the bash file.

    (bashファイルを実行することでroscore・パブリッシャ・すべてのサブスクライバを起動することができます。)
    ```
    $ cd ~/catkin_ws/src/translate
    $ ./start.bash
    ```
---
## Works cited
-   Prof. Ryuichi Ueda
    -   robosys2020 - ros
        -   [md](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)

        -   [Youtube](https://youtu.be/PL85Pw_zQH0)

    -   [ros_setup_scripts_Ubuntu20.04_desktop](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop)

-   [Text Translation with Google Translate API in Python](https://stackabuse.com/text-translation-with-google-translate-api-in-python/)

-    [error in result (AttributeError: 'NoneType' object has no attribute 'group')](https://github.com/ssut/py-googletrans/issues/234#issuecomment-742460612)

-   [googletrans 4.0.0rc1](https://pypi.org/project/googletrans/4.0.0rc1/)

---
## LICENSE
- ROS - [BSD](https://github.com/MasatoKubotera/translate/blob/master/LICENSE)

- googletrans - [MIT](https://pypi.org/project/googletrans/4.0.0rc1/)
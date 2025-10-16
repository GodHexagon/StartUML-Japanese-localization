#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys

# 日本語翻訳マッピング
translations = {
    # Main menus
    "File": "ファイル",
    "Edit": "編集",
    "Format": "書式",
    "Model": "モデル",
    "Tools": "ツール",
    "View": "表示",
    "Window": "ウィンドウ",
    "Help": "ヘルプ",

    # File menu
    "New": "新規作成",
    "New From Template": "テンプレートから新規作成",
    "Open...": "開く...",
    "Open Recent": "最近使ったファイル",
    "Save": "保存",
    "Save As...": "名前を付けて保存...",
    "Close": "閉じる",
    "Import": "インポート",
    "Export": "エクスポート",
    "Fragment...": "フラグメント...",
    "Export Diagram As": "ダイアグラムをエクスポート",
    "PNG...": "PNG...",
    "JPEG...": "JPEG...",
    "SVG...": "SVG...",
    "All to PNGs...": "すべてPNGに...",
    "All to JPEGs...": "すべてJPEGに...",
    "All to SVGs...": "すべてSVGに...",
    "Preferences...": "環境設定...",
    "Print to PDF...": "PDFに印刷...",
    "Exit": "終了",

    # Edit menu
    "Undo": "元に戻す",
    "Redo": "やり直す",
    "Cut": "切り取り",
    "Copy": "コピー",
    "Copy Diagram As Image": "ダイアグラムを画像としてコピー",
    "Paste": "貼り付け",
    "Delete": "削除",
    "Delete From Model": "モデルから削除",
    "Move Up": "上へ移動",
    "Move Down": "下へ移動",
    "Select All": "すべて選択",
    "Select In Explorer": "エクスプローラーで選択",
    "Select In Diagram": "ダイアグラムで選択",
    "Open Sub-Diagram": "サブダイアグラムを開く",

    # Format menu
    "Font...": "フォント...",
    "Fill Color...": "塗りつぶし色...",
    "Line Color...": "線の色...",
    "Line Style": "線のスタイル",
    "Rectilinear": "直角",
    "Oblique": "斜め",
    "RoundRect": "角丸直角",
    "Curve": "曲線",
    "Auto Resize": "自動リサイズ",
    "Show Shadow": "影を表示",

    # Model menu
    "Add Diagram": "ダイアグラムを追加",
    "Add": "追加",
    "Tag Editor...": "タグエディター...",

    # Tools menu
    "Extension Manager...": "拡張機能マネージャー...",

    # View menu
    "Quick Find...": "クイック検索...",
    "Command Palette...": "コマンドパレット...",
    "Close Diagram": "ダイアグラムを閉じる",
    "Close Other Diagrams": "他のダイアグラムを閉じる",
    "Close All Diagrams": "すべてのダイアグラムを閉じる",
    "Next Diagram": "次のダイアグラム",
    "Previous Diagram": "前のダイアグラム",
    "Zoom In": "拡大",
    "Zoom Out": "縮小",
    "Actual Size": "実際のサイズ",
    "Fit To Window": "ウィンドウに合わせる",
    "Show Grid": "グリッドを表示",
    "Snap to Grid": "グリッドにスナップ",
    "Sidebar": "サイドバー",
    "Navigator": "ナビゲーター",
    "Toolbar": "ツールバー",
    "Statusbar": "ステータスバー",
    "Toolbox": "ツールボックス",
    "Editors": "エディター",

    # Window menu
    "Minimize": "最小化",
    "Full Screen": "フルスクリーン",
    "Bring All to Front": "すべてを前面に",

    # Help menu
    "About StarUML": "StarUMLについて",
    "Check For Updates...": "更新の確認...",
    "Enter License Key...": "ライセンスキーの入力...",
    "Delete License Key...": "ライセンスキーの削除...",
    "Documentation...": "ドキュメント...",
    "Forum...": "フォーラム...",
    "Request Feature...": "機能リクエスト...",

    # Context menu specific
    "Rename": "名前を変更",
    "Sort By Added": "追加順にソート",
    "Sort By Name": "名前順にソート",
    "Show Stereotype Text": "ステレオタイプテキストを表示",
    "Expand All": "すべて展開",
    "Collapse All": "すべて折りたたむ"
}

def translate_menu(obj):
    """Recursively translate menu labels"""
    if isinstance(obj, dict):
        new_obj = {}
        for key, value in obj.items():
            if key == "label" and value in translations:
                new_obj[key] = translations[value]
            elif isinstance(value, (dict, list)):
                new_obj[key] = translate_menu(value)
            else:
                new_obj[key] = value
        return new_obj
    elif isinstance(obj, list):
        return [translate_menu(item) for item in obj]
    else:
        return obj

def main():
    if len(sys.argv) < 3:
        print("Usage: python translate-menu.py input.json output.json")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read input JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Translate
    translated_data = translate_menu(data)

    # Write output JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)

    print(f"Translation complete: {input_file} -> {output_file}")

if __name__ == "__main__":
    main()

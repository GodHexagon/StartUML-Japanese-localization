# StarUML 日本語化ガイド

このドキュメントでは、StarUMLを日本語化する方法を詳しく説明します。

## 目次

1. [概要](#概要)
2. [必要なもの](#必要なもの)
3. [日本語化の仕組み](#日本語化の仕組み)
4. [インストール手順](#インストール手順)
5. [トラブルシューティング](#トラブルシューティング)
6. [元に戻す方法](#元に戻す方法)
7. [技術的な詳細](#技術的な詳細)

---

## 概要

StarUMLは標準では英語UIですが、内部のメニュー定義ファイルを日本語化することで、完全に日本語化できます。

### 日本語化される内容

- メインメニュー（ファイル、編集、表示、書式、モデル、ツール、ヘルプ）
- すべてのサブメニュー項目
- 右クリックコンテキストメニュー
- ダイアログのボタンやメッセージ

---

## 必要なもの

- **StarUML** がインストールされていること
- **管理者権限** でコマンドを実行できること
- 以下のファイル（このガイドと同じフォルダにあります）:
  - `app-japanese.asar` - 日本語化されたアプリケーションパッケージ
  - `Install-StarUML-Japanese.ps1` - PowerShellインストールスクリプト
  - `install-japanese-final.bat` - バッチインストールスクリプト

---

## 日本語化の仕組み

StarUMLはElectronベースのアプリケーションで、以下の構造になっています：

```
C:\Program Files\StarUML\
├── resources/
│   ├── app.asar              ← アプリケーション本体（これを置き換える）
│   └── default/
│       └── menus/
│           └── win32.json    ← メニュー定義（日本語化済み）
└── StarUML.exe
```

### なぜstrings.jsだけでは不十分だったのか

当初、`src/strings.js`ファイルを日本語化しましたが、これはダイアログやメッセージの翻訳に使われるだけで、メニューには影響しませんでした。

**実際のメニューは `resources/default/menus/win32.json` で定義されています。**

このJSONファイルの `"label"` フィールドがメニューに直接表示されるため、このファイルを日本語化する必要がありました。

---

## インストール手順

### 方法1: PowerShellスクリプト（推奨）

最も簡単で確実な方法です。

#### 手順

1. **管理者権限でPowerShellを起動**
   - スタートメニューで「PowerShell」を検索
   - 右クリック → 「管理者として実行」を選択

2. **ユーザーのホームディレクトリに移動**
   ```powershell
   cd $env:USERPROFILE
   ```

3. **インストールスクリプトを実行**
   ```powershell
   .\Install-StarUML-Japanese.ps1
   ```

4. **実行ポリシーエラーが出た場合**

   以下のコマンドを実行してから、再度スクリプトを実行してください：
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

5. **StarUMLを再起動**
   - 既にStarUMLが起動している場合は、完全に終了してください
   - タスクマネージャーでプロセスが残っていないことを確認
   - StarUMLを起動すると、メニューが日本語で表示されます！

---

### 方法2: バッチファイル

コマンドプロンプトを使う方法です。

#### 手順

1. **管理者権限でコマンドプロンプトを起動**
   - スタートメニューで「cmd」を検索
   - 右クリック → 「管理者として実行」を選択

2. **バッチファイルを実行**
   ```cmd
   C:\Users\user\install-japanese-final.bat
   ```

3. **StarUMLを再起動**

---

### 方法3: 手動インストール

スクリプトを使わず、手動でファイルをコピーする方法です。

#### 手順

1. **管理者権限でコマンドプロンプトを起動**

2. **元のファイルをバックアップ**
   ```cmd
   copy "C:\Program Files\StarUML\resources\app.asar" "C:\Program Files\StarUML\resources\app.asar.backup"
   ```

3. **日本語化ファイルをコピー**
   ```cmd
   copy /Y "%USERPROFILE%\app-japanese.asar" "C:\Program Files\StarUML\resources\app.asar"
   ```

4. **StarUMLを再起動**

---

## トラブルシューティング

### 1. 「アクセスが拒否されました」エラー

**原因**: 管理者権限で実行していない

**解決方法**:
- PowerShellまたはコマンドプロンプトを**必ず管理者として実行**してください
- プログラムファイルフォルダへの書き込みには管理者権限が必要です

---

### 2. 「app-japanese.asarが見つかりません」エラー

**原因**: ファイルが正しい場所にない

**解決方法**:
- `app-japanese.asar`ファイルが `C:\Users\user\` にあることを確認
- PowerShellで以下を実行して確認：
  ```powershell
  Test-Path "$env:USERPROFILE\app-japanese.asar"
  ```
- `True`と表示されればOK、`False`の場合はファイルをコピーしてください

---

### 3. 日本語化されない

**原因**: StarUMLのキャッシュが残っている

**解決方法**:
1. タスクマネージャーでStarUMLプロセスを完全に終了
2. StarUMLの設定フォルダをクリア（オプション）:
   ```
   %APPDATA%\StarUML
   ```
3. StarUMLを再起動

---

### 4. 一部だけ日本語化されている

**原因**: メニューは日本語化されますが、一部のダイアログやエラーメッセージは英語のままです

**説明**:
- メインメニューとコンテキストメニューは完全に日本語化されます
- ダイアログやメッセージの一部は、拡張機能によって追加されているため、英語のままの場合があります

---

## 元に戻す方法

日本語化を取り消して、英語版に戻す方法です。

### PowerShellの場合

管理者権限のPowerShellで実行：

```powershell
Copy-Item -Path "C:\Program Files\StarUML\resources\app.asar.backup" -Destination "C:\Program Files\StarUML\resources\app.asar" -Force
```

### コマンドプロンプトの場合

管理者権限のコマンドプロンプトで実行：

```cmd
copy /Y "C:\Program Files\StarUML\resources\app.asar.backup" "C:\Program Files\StarUML\resources\app.asar"
```

その後、StarUMLを再起動すれば英語版に戻ります。

---

## 技術的な詳細

### StarUMLの構造

StarUMLはElectronベースのアプリケーションで、以下のような構造になっています：

```
app.asar (ASARアーカイブファイル)
├── package.json
├── src/
│   ├── app-context.js           ← アプリケーション初期化
│   ├── strings.js               ← ダイアログ用文字列定義
│   ├── main-process/
│   │   ├── application-menu.js  ← メニュー管理
│   │   └── main.js
│   └── ui/
│       ├── menu-manager.js      ← メニューマネージャー
│       └── menu-helpers.js
└── resources/
    └── default/
        └── menus/
            ├── win32.json       ← Windowsメニュー定義 ★重要
            ├── darwin.json      ← macOSメニュー定義
            └── linux.json       ← Linuxメニュー定義
```

### メニュー読み込みの仕組み

`src/app-context.js`の初期化コードで、以下のようにメニューを読み込んでいます：

```javascript
// プラットフォームに応じたメニューファイルを読み込む
let menus = require(`../resources/default/menus/${process.platform}.json`);
this.menu.add(menus["menu"]);
```

Windowsの場合は `process.platform` が `"win32"` なので、`win32.json`が読み込まれます。

### 日本語化プロセス

1. **app.asarアーカイブを展開**
   ```bash
   npx asar extract app.asar StarUML-extracted
   ```

   普通は、app.asarがここにインストールされている: `C:\Program Files\StarUML\resources\app-update.yml`

2. **メニューファイルを日本語化**

   `translate-menu.py`スクリプトを使用して、`win32.json`の全ての`"label"`フィールドを日本語に変換：

   ```python
   translations = {
       "File": "ファイル",
       "Edit": "編集",
       "View": "表示",
       # ... など
   }
   ```

3. **app.asarを再パッケージ化**
   ```bash
   npx asar pack StarUML-extracted app-japanese.asar
   ```

4. **StarUMLのapp.asarと置き換え**

### 翻訳マッピング

`translate-menu.py`で使用している主な翻訳マッピング：

| 英語 | 日本語 |
|------|--------|
| File | ファイル |
| Edit | 編集 |
| Format | 書式 |
| Model | モデル |
| Tools | ツール |
| View | 表示 |
| Window | ウィンドウ |
| Help | ヘルプ |
| New | 新規作成 |
| Open | 開く |
| Save | 保存 |
| Copy | コピー |
| Paste | 貼り付け |
| Delete | 削除 |

完全なリストは`translate-menu.py`を参照してください。

---

## 再配布について

このパッケージを他の人と共有する場合、以下のファイルをまとめて配布してください：

- `app-japanese.asar` - 日本語化されたアプリケーション
- `Install-StarUML-Japanese.ps1` - PowerShellインストーラー
- `install-japanese-final.bat` - バッチインストーラー
- `StarUML日本語化ガイド.md` - このドキュメント

---

## よくある質問（FAQ）

### Q1. StarUMLをアップデートしたら英語に戻ってしまいました

**A**: StarUMLを更新すると`app.asar`が上書きされるため、日本語化が解除されます。更新後に再度日本語化スクリプトを実行してください。

### Q2. macOSやLinuxでも使えますか？

**A**: このガイドはWindows向けですが、同じ方法でmacOS（`darwin.json`）やLinux（`linux.json`）でも日本語化できます。

### Q3. 拡張機能のメニューも日本語化されますか？

**A**: いいえ。拡張機能が独自に追加するメニュー項目は、その拡張機能側で定義されているため、このパッケージでは日本語化されません。

### Q4. ライセンスキーは保持されますか？

**A**: はい。ライセンス情報は別の場所に保存されているため、日本語化しても影響ありません。

### Q5. 安全ですか？

**A**: はい。このパッケージは既存のファイルを置き換えるだけで、StarUMLの機能を変更したり、追加のソフトウェアをインストールしたりすることはありません。元のファイルはバックアップされます。

---

## 更新履歴

- **2024-10-16**: 初版作成
  - Windows向けメニュー完全日本語化
  - PowerShellインストーラー追加
  - バッチインストーラー追加

---

## サポート

問題が発生した場合や質問がある場合は、以下を確認してください：

1. このドキュメントの[トラブルシューティング](#トラブルシューティング)セクション
2. バックアップファイル（`app.asar.backup`）が存在することを確認
3. 管理者権限で実行していることを確認

---

## ライセンスと免責事項

このパッケージは個人的な使用のために作成されました。StarUML本体のライセンスには影響しません。

**免責事項**: このパッケージの使用は自己責任でお願いします。作成者は、このパッケージの使用によって生じたいかなる損害についても責任を負いません。

---

**日本語化されたStarUMLをお楽しみください！**

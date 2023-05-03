
.PHONY: setup
setup: # virtualenv 環境を作成し, ライブラリをインストールする.
	@bash src/scripts/virtualenv-runner.sh setup

.PHONY: repl
repl: # python の repl を開始する.
	@bash src/scripts/virtualenv-runner.sh repl

.PHONY: run
run: # アプリケーションを実行する.
	@bash src/scripts/virtualenv-runner.sh run


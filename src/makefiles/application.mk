
.PHONY: setup
setup: # virtualenv 環境を作成し, ライブラリをインストールする.
	@bash src/scripts/virtualenv-runner.sh setup

.PHONY: clean
clean: # 中間ファイルを削除する.
	@rm -rf target

.PHONY: repl
repl: # python の repl を開始する.
	@bash src/scripts/virtualenv-runner.sh repl

.PHONY: run
run: # アプリケーションを実行する.
	@bash src/scripts/virtualenv-runner.sh run

.PHONY: test
test: # テストを実行する.
	@bash src/scripts/virtualenv-runner.sh test

.PHONY: coverage
coverage: # テストのカバレッジを計測する.
	@bash src/scripts/virtualenv-runner.sh coverage


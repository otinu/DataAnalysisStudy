import traceback

def print_error(be):
    print("【エラー原因】")
    print(be)
    print("\n【エラー発生行】")
    traceback.print_exc()
    pass
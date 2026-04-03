import pandas as pd
from pathlib import Path

# 项目根目录
ROOT = Path(__file__).resolve().parents[2]

def load_ieee(verbose=True):
    """
    读取 IEEE-CIS 原始数据并合并 transaction + identity
    返回合并后的 DataFrame，按 TransactionDT 排序
    """
    trans_path = ROOT / "data" / "raw" / "ieee" / "train_transaction.csv"
    id_path    = ROOT / "data" / "raw" / "ieee" / "train_identity.csv"

    if verbose:
        print("正在读取 train_transaction.csv ...")
    df_trans = pd.read_csv(trans_path)

    if verbose:
        print("正在读取 train_identity.csv ...")
    df_id = pd.read_csv(id_path)

    if verbose:
        print("正在合并 ...")
    df = df_trans.merge(df_id, on="TransactionID", how="left")
    df = df.sort_values("TransactionDT").reset_index(drop=True)

    if verbose:
        print(f"合并完成：{df.shape[0]:,} 行，{df.shape[1]} 列")
        print(f"欺诈比例：{df['isFraud'].mean()*100:.3f}%")

    return df


def load_paysim(verbose=True):
    """
    读取 PaySim 原始数据
    返回按 step 排序的 DataFrame
    """
    path = ROOT / "data" / "raw" / "paysim" / "paysim.csv"

    if verbose:
        print("正在读取 paysim.csv ...")
    df = pd.read_csv(path)
    df = df.sort_values("step").reset_index(drop=True)

    if verbose:
        print(f"读取完成：{df.shape[0]:,} 行，{df.shape[1]} 列")
        print(f"欺诈比例：{df['isFraud'].mean()*100:.3f}%")

    return df
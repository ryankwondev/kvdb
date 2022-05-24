from fastapi import FastAPI, Response
import sqlite3

app = FastAPI()

database = sqlite3.connect(":memory:")
cursor = database.cursor()


def CreateTable(tbl: str):
    cursor.execute(f"""
    create table "{tbl}"
    (
    key text not null
        constraint "{tbl}_pk"
            primary key,
    value text
    );
    """)
    cursor.execute(f"""
    create unique index "{tbl}_key_uindex"
        on "{tbl}" (key);
    """)
    database.commit()


@app.get("/")
async def root():
    return {"message": "대충 혼자-회사에서- 쓰려고 만든거니까 코드퀄리티 좆말아먹을거임ㅋㅋ"}


@app.post("/{table}/")
async def CreateResource(key: str, value: str, response: Response, table: str):
    # table의 존재 여부 확인
    CreateTable("dwaw")
    res = cursor.execute(f"SELECT * FROM sqlite_master WHERE type='table' AND tbl_name='{table}';")
    return res.rowcount
    #     CreateTable(table) # 만들어서 써라
    #
    # print(res)
    #
    # cursor.execute(f"INSERT INTO {table} (key, value) VALUES ('{key}', '{value}');")
    # database.commit()
    #
    # response.status_code = 200
    # return cursor.execute(f"SELECT * FROM {table} WHERE Key={key}")

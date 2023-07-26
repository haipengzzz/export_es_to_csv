from elasticsearch import Elasticsearch
import csv


def export_index_to_csv(es_host, es_port, es_username, es_password, index_name, keyword, page_size=10000):
    es = Elasticsearch(
        [f"{es_host}:{es_port}"],
        http_auth=(es_username, es_password),verify_certs=False,
    )
    query = {
        "query": {
            "match": {
                "ecs.version": keyword
            }
        }
    }

    output_file = f"{index_name}_export.csv"
    scroll = '2m'  # 设置滚动时间窗口为2分钟，否则可能会导致内存溢出
    result = es.search(index=index_name, body=query, size=page_size, scroll=scroll)

    # 分页遍历并导出为CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入CSV文件的表头
        writer.writerow(["timestamp", "host","os","message"])
        sid = result['_scroll_id']
        total_hits = result['hits']['total']['value']

        while total_hits > 0:
            hits = result["hits"]["hits"]
            for hit in hits:
                try:
                    # 这里需要根据你的索引结构来获取相应的字段值，例如hit["_source"]["timestamp"]
                    row = [
                        hit["_source"]["@timestamp"],
                        hit['_source']['host']['hostname'],
                        hit['_source']['host']['os'],
                    ]
                    writer.writerow(row)
                except KeyError as e:
                    # 如果出现KeyError异常，执行这里的代码块
                    print(f"Encountered KeyError: {e}. Skipping this entry.")
                    result = es.scroll(scroll_id=sid, scroll=scroll)
                    sid = result['_scroll_id']
                    total_hits -= len(hits)

    print(f"导出完成，结果保存在 {output_file}")
if __name__ == "__main__":
    host = "" 
    port = 9200 
    username = "" 
    password = ""  
    index_name = ""  # 替换为你要查询的索引名称
    keyword = "1.9.0"  # 替换为你要查询的关键字
    export_index_to_csv(host, port, username, password, index_name, keyword)
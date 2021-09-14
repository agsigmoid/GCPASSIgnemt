try:
    import pandas as pd
    from google.cloud import bigquery
    from Constants.Path import PATH
    from google.cloud import storage
    from pandas.io import gbq
except Exception as e:
    print(f"{e} found in this module")

client=bigquery.Client.from_service_account_json(json_credentials_path=f'{PATH}/gcp-assignment-322710-7ee5c22d656b.json')


def MergeCSV(file1,file2):
    df1=pd.read_csv(file1)
    df2=pd.read_csv(file2)
    res=pd.merge(left=df1,right=df2,how="left",on="CustomerID")
    return res

def createDataset(client,projectid='gcp-assignment-322710'):

    try:
        dataset_id=f"{projectid}.ag_dataset"
        dataset = bigquery.Dataset(dataset_id)
        dataset = client.create_dataset(dataset, timeout=30)
        print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
    except Exception as e:
        print(e)

def CreateTable(client,projectid='gcp-assignment-322710'):
    try:
        table_id=f"{projectid}.ag_dataset.results"
        table = bigquery.Table(table_id)
        table = client.create_table(table)
        print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))
    except Exception as e:
        print(e)

# number of dataset available in our Project
def ListOfDataSet(client):
    datasets = list(client.list_datasets())  # Make an API request.
    print(client.project)
    project = client.project

    if datasets:
        print("Datasets in project {}:".format(project))
        for dataset in datasets:
            print("\t{}".format(dataset.dataset_id))
    else:
        print("{} project does not contain any datasets.".format(project))

def QueryingdataSet(client):
    query = """
        SELECT CustomerID
        FROM `gcp-assignment-322710.ag_dataset.results`
        WHERE country = 'UK'
        group by CustomerID
        LIMIT 200
    """
    query_job = client.query(query)  # Make an API request.

    print("The query data:")
    for row in query_job:
        print(row)
        # Row values can be accessed by field name or index.
        # print("name={}, count={}".format(row["CustomerID"], row["OrderID"]))

def loadData(res):
    df1=res
    # df1=pd.read_csv("results.csv");
    print(df1.head())
    df1.to_gbq(destination_table="ag_dataset.results",project_id='gcp-assignment-322710',if_exists="replace")
    print("files loaded into results")

if __name__=="__main__":
    # QueryingdataSet(client)
    # ListOfDataSet(client)
    createDataset(client)
    CreateTable(client)
    file1=f"{PATH}/Orders.csv"
    file2=f"{PATH}/Customers.csv"
    #print(file1,file2,sep="\n")
    res=MergeCSV(file1,file2)
    loadData(res)
    res.to_csv("results.csv",index=False)



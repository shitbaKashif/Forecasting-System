import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        dataset = request.form.get('dataset')
        model = request.form.get('model')
        if not model:  # If no model is selected, display all models for the selected dataset
            return render_template("result.html", dataset=dataset, models=data[dataset])
        return render_template("result.html", dataset=dataset, model=model)
    
    # Load dataset and model options from data2.json
    with open('static/data.json', 'r') as file:
        data = json.load(file)
    datasets = list(data.keys())
    models = list(data[datasets[0]].keys())
    
    return render_template("home.html", datasets=datasets, models=models)


@app.route('/result', methods=['POST'])
def result():
    print("Result function called")

    selected_dataset = request.form['dataset']
    selected_model = request.form['model']

    # Load data from the data2.json file
    with open('static/data.json', "r") as json_file:
        data = json.load(json_file)
    print("Result function called 22")

    # Extract model data for the selected dataset and model
    dataset_data = data.get(selected_dataset, {})
    model_data = dataset_data.get(selected_model, {})
    print("Result function called 33")
    print(model_data)
    # Initialize variables
    parameters = {}
    rmse = 0
    loss = 0
    images = []
    ev = {} 
    print("Result function called 44")
    dq=[]
    # Try to extract parameters, RMSE, loss, and images
    try:
        ev = {key: value for key, value in model_data.items() if key != 'image'}
        print("ev", ev)
    except Exception as e:
        print(f"Error: {e}")
    try:
        parameters = model_data["best_params"]
        print("p", parameters)
        
    except Exception as e:
        print(f"Error: {e}")
    try:   
        rmse = model_data.get("rmse", 0)
        print("r", rmse)
    except Exception as e:
        print(f"Error: {e}")
    try:    
        loss = model_data.get("loss", 0)
        print(loss, "l")
    except Exception as e:
        print(f"Error: {e}")
    try:    
        images = model_data.get("image", [])
        print(images, "i")
    except Exception as e:
        print(f"Error: {e}")

    return render_template('result.html', dataset=selected_dataset, model=selected_model, ev=ev,
                           parameters=parameters, rmse=rmse, loss=loss, images=images)


if __name__ == '__main__':
    app.run(debug=True)

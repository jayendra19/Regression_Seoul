from flask import Flask,request,render_template,jsonify

from src.pipeline.predict_pipeline import CustomData,PredictPipeline
#from sklearn.preprocessing import StandardScaler

applications =Flask(__name__)

app=applications

#Route for homepage

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
            hour=int(request.form.get('hour')),
            temperature=float(request.form.get('temperature')),
            wind_speed_m_s=float(request.form.get('wind_speed')) if request.form.get('wind_speed') is not None else 0.0,
            visibility_10m=float(request.form.get('visibility')) if request.form.get('visibility') is not None else 0.0,
            solar_radiation_mj_m2=float(request.form.get('solar_radiation'))if request.form.get('solar_radiation') is not None else 0.0,
            rainfall_mm=float(request.form.get('rainfall'))if request.form.get('rainfall') is not None else 0.0,
            snowfall_cm=float(request.form.get('snowfall'))if request.form.get('snowfall') is not None else 0.0,
            seasons=request.form.get('seasons'),
            holiday=request.form.get('holiday'),
            functioning_day=request.form.get('functioning_day'),
            year=int(request.form.get('year')),
            day=int(request.form.get('day')),
            months=int(request.form.get('months')),
            weekday=request.form.get('weekday'),
        )

        pred_df=data.get_data_as_frame()
        print(pred_df)
        print("before prdiction")

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)

        return render_template('home.html',results=int(results[0]))
    

@app.route('/predictapi', methods=['POST'])
def predict_bike_count():
    try:
        # Get input data from the request
        data = request.get_json()

        # Created CustomData object from input
        custom_data = CustomData(**data)

        # Get predictions using the pipeline
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(custom_data.get_data_as_frame())

        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)






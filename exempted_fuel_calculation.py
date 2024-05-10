html_content = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>면세유 계산</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            width: 700px;
            padding: 40px;
            text-align: center;
            border: 2px solid #61dafb;
        }
        h1 {
            color: #61dafb;
            margin-bottom: 30px;
        }
        label {
            color: #495057;
            font-weight: bold;
        }
        input[type="number"] {
            margin-bottom: 15px;
        }
        .btn-calculate {
            background-color: #61dafb;
            border: none;
            margin-top: 15px;
            transition: background-color 0.3s ease;
            color: white;
            font-weight: bold;
        }
        .btn-calculate:hover {
            background-color: #21a1f1;
        }
        .btn-reset {
            background-color: #ff4c4c;
            border: none;
            margin-top: 15px;
            transition: background-color 0.3s ease;
            color: white;
            font-weight: bold;
        }
        .btn-reset:hover {
            background-color: #d12f2f;
        }
        #result {
            margin-top: 25px;
            color: #ff4c4c;
            font-weight: bold;
            font-size: 20px;
        }
    </style>
    <script>
        function calculate() {
            
            var fishing_line = parseFloat(document.getElementById('fishing_line').value) || 0;
            var trap = parseFloat(document.getElementById('trap').value) || 0;
            var pet = parseFloat(document.getElementById('pet').value) || 0;
            var net = parseFloat(document.getElementById('net').value) || 0;
            var plastic = parseFloat(document.getElementById('plastic').value) || 0;
            var rope = parseFloat(document.getElementById('rope').value) || 0;
            var styrofoam = parseFloat(document.getElementById('styrofoam').value) || 0;
            var tire = parseFloat(document.getElementById('tire').value) || 0;
            var wood = parseFloat(document.getElementById('wood').value) || 0;
            var fuel_usage = parseFloat(document.getElementById('fuel_usage').value) || 0;

            
            var result = fishing_line * 0.602659 + trap * 0.602637 + pet * 0.451923 + net * 0.602659 +
                         plastic * 0.643957 + rope * 0.626402 + styrofoam * 0.53316 + tire * 0.42133 +
                         wood * 0.723208 + fuel_usage * 0.5;

            
            document.getElementById('result').innerText = '면세유 지급용량: ' + result.toFixed(2) + ' 리터';
        }

        function resetFields() {
            document.getElementById('fishing_line').value = '';
            document.getElementById('trap').value = '';
            document.getElementById('pet').value = '';
            document.getElementById('net').value = '';
            document.getElementById('plastic').value = '';
            document.getElementById('rope').value = '';
            document.getElementById('styrofoam').value = '';
            document.getElementById('tire').value = '';
            document.getElementById('wood').value = '';
            document.getElementById('fuel_usage').value = '';
            document.getElementById('result').innerText = '';
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>면세유 계산</h1>
        <div class="form-row">
            <div class="form-group col-md-6">
                <label for="fishing_line">낚시줄:</label>
                <input type="number" id="fishing_line" class="form-control" placeholder="0">
                <label for="trap">통발:</label>
                <input type="number" id="trap" class="form-control" placeholder="0">
                <label for="pet">PET:</label>
                <input type="number" id="pet" class="form-control" placeholder="0">
                <label for="net">그물망:</label>
                <input type="number" id="net" class="form-control" placeholder="0">
                <label for="plastic">플라스틱:</label>
                <input type="number" id="plastic" class="form-control" placeholder="0">
            </div>
            <div class="form-group col-md-6">
                <label for="rope">밧줄:</label>
                <input type="number" id="rope" class="form-control" placeholder="0">
                <label for="styrofoam">스티로폼:</label>
                <input type="number" id="styrofoam" class="form-control" placeholder="0">
                <label for="tire">타이어:</label>
                <input type="number" id="tire" class="form-control" placeholder="0">
                <label for="wood">나무:</label>
                <input type="number" id="wood" class="form-control" placeholder="0">
                <label for="fuel_usage">연료 사용량 (리터):</label>
                <input type="number" id="fuel_usage" class="form-control" placeholder="0">
            </div>
        </div>
        <button class="btn btn-calculate" onclick="calculate()">계산하기</button>
        <button class="btn btn-reset" onclick="resetFields()">RESET</button>
        <p id="result"></p>
    </div>
</body>
</html>
"""


with open('exempted_fuel_calculation.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML file has been created.")

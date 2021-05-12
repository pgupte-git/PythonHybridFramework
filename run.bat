rem pytest -v -s -m "sanity" --capture=sys --html=./Reports/report.html TestCases/ --browsername chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
rem pytest -v -s -m "regression" --capture=sys --html=./Reports/report.html TestCases/ --browsername chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
rem pytest -v -s -m "sanity and regression" --capture=sys --html=./Reports/report.html TestCases/ --browsername chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
rem pytest -v -s -m "sanity or regression" --capture=sys --html=./Reports/report.html TestCases/ --browsername chrome --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F


pytest -v -s -m "sanity" --capture=sys --html=./Reports/report.html TestCases/ --browsername firefox --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
rem pytest -v -s -m "regression" --capture=sys --html=./Reports/report.html TestCases/ --browsername firefox --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
rem pytest -v -s -m "sanity and regression" --capture=sys --html=./Reports/report.html TestCases/ --browsername firefox --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
rem pytest -v -s -m "sanity or regression" --capture=sys --html=./Reports/report.html TestCases/ --browsername firefox --url https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
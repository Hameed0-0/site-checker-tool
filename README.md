# site-checker-tool 

```markdown
# Site Checker Tool

**Site Checker Tool** is a simple Python-based tool that allows you to check broken links on a website. It generates reports in **PDF** and **JSON** formats, helping you identify and fix issues with website links.

## Features
- Check all the links (URLs) on a website.
- Identify broken links (404 errors).
- Generate detailed reports in **PDF** and **JSON** formats.
- Easy-to-use with clear output for website maintenance.

## Installation

To get started, follow these steps:

### 1. Clone the repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/YourUsername/site-checker-tool.git
cd site-checker-tool
```

### 2. Install the required dependencies
Make sure you have **Python** and **pip** installed. Then, install the required Python libraries by running:
```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt` yet, you can generate it by running:
```bash
pip freeze > requirements.txt
```

This will include libraries such as:
- **requests**: For making HTTP requests.
- **beautifulsoup4**: For parsing HTML content.
- **fpdf**: For generating PDF reports.
- **lxml**: For better performance in parsing HTML.

## Usage

1. **Run the script**:
   After installing the dependencies, run the following command to check the links on a website:
   ```bash
   python site_checker.py
   ```

2. **Enter the URL**:
   When prompted, enter the website URL you want to check (e.g., `https://example.com`).

3. **View the results**:
   The script will display the broken links in the terminal. It will also generate two reports:
   - **PDF Report**: `report.pdf` — A professional PDF report listing all broken links.
   - **JSON Report**: `report.json` — A JSON file containing detailed information about the broken links.

## Example Output

If broken links are found, the script will output a list of broken URLs in the terminal and save the following reports:
- **report.pdf**: A detailed PDF document containing the broken links.
- **report.json**: A JSON file containing the list of broken links and the website name.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions, improvements, or bug fixes. To contribute:
1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes and push to your forked repository.
4. Open a pull request.

## Contact

For any questions or feedback, please feel free to open an issue on this repository or contact me via email.

---
Thank you for using **Site Checker Tool**! Keep your websites in check and avoid broken links!
```

import zipfile
import xml.etree.ElementTree as ET

def extract_sensitivity_label_from_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as docx:
            found = False
            for name in docx.namelist():
                if "custom.xml" in name:
                    content = docx.read(name)
                    root = ET.fromstring(content)

                    for elem in root.iter():
                        if elem.text and any(label in elem.text.lower() for label in ["confidential", "classified", "sensitivity", "msip"]):
                            print(f"✅ Sensitivity Label found in ({name}): {elem.text}")
                            found = True
            if not found:
                print("❌ No sensitivity label (e.g., 'Confidential') found in this document.")
    except zipfile.BadZipFile:
        print("⚠️ This is not a valid .docx file.")
    except Exception as e:
        print(f"❌ Error parsing XML in file: {e}")

#after merge
#after conecting to github 
# after origin
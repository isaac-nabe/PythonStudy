def main():

    # Dictionary of file extensions & their media types
    media_types_Dict = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Prompts user for the file name
    file_name = input("File Name: ").lower().strip()

    # Finds the media type based on ext's
    m_type = media_types_Dict.get(file_name[file_name.rfind("."):], "application/octet-stream")

    #media_types_Dict is the dictionary we're extracting data from.
    #file_name.rfind(".") locates the "."
    #file_name[...:] then grabs everything after the "."

    #Tacking on the ".get()" function to media_types_Dict
    #allows us to grab the keyname of the item we want to return the value from (file_name + extension).
    #In this case the various media types, & Luckily anything after the comma (e.g. y in ".get(x, y)") ...
    #is treated as a value to return if the specified keyname (file_name + extension) doesn't exist within the dictionary.

    #Therefore, we can put our default message here to pop up when the key word doesn't apply to the values in the dictionary.


    # Output the media type
    print(m_type)

main()

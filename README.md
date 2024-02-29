# grayscale
This program converts directories from RGB -> GrayScale 

<table>
  <tr>
    <td align="center">
      <b>RGB</b><br>
      <img src="https://github.com/AlessandroB1298/grayscale/assets/98426727/f35a9a21-3dfa-4dce-8afc-71a2d61abd0c" width="450" alt="RGB" />
    </td>
    <td align="center">
      <b>Grayscale</b><br>
      <img src="https://github.com/AlessandroB1298/grayscale/assets/98426727/fd9ad28a-2743-40dd-825e-c9aacaca20fd" width="450" alt="Grayscale" />
    </td>
  </tr>
</table>


### This program uses opencv to convert images from RBG to Grayscale 
```ruby
  gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #cv.cvtColor(src, code[, dst[, dstCn]]) -> dst
  output_path = os.path.join(output_folder, f) # join to the output path
  cv.imwrite(output_path, gray_img)

```
### This program only handles directories and check this list to make sure you are using the correct versions

```ruby
numpy==1.26.4
opencv-python==4.9.0.80
pillow==10.2.0
tqdm==4.66.2

```

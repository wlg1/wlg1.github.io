# LaTeX

- in latex, why use pdf for images?
    
    Using PDF for images in LaTeX documents has several advantages:
    
    ### Vector Graphics
    
    1. **Scalability**: PDF can contain vector graphics, meaning the image can be resized without any loss in quality. This is especially useful for diagrams and illustrations where high-quality scaling is needed.
    2. **File Size**: Vector graphics are generally smaller in size compared to high-resolution raster images.
    
    ### Compatibility
    
    1. **Native Support**: PDFLaTeX, which is commonly used for compiling LaTeX documents, has native support for PDF, JPG, and PNG, but older compilers like LaTeX or DVI modes do not natively support as many formats.
    2. **Text Rendering**: If your image includes text, it will generally be rendered more clearly in PDF format, especially when printed.
    
    ### Transparency
    
    1. **Transparency**: PDF supports transparent backgrounds, which can be an advantage when you want to overlay your image onto a colored or patterned background in your LaTeX document.
    
    ### Color Accuracy
    
    1. **Color Management**: PDF supports robust color management, ensuring that the colors in the image are displayed and printed as intended.
    
    ### Multiple Pages
    
    1. **Multi-page**: PDF files can contain multiple pages, so you can include multi-page diagrams or illustrations within a single PDF file and then include them selectively in your LaTeX document.
    
    ### Universality
    
    1. **Standard Format**: PDF is a widely-used standard, which makes sharing and archiving easy.
    
    ### Software Support
    
    1. **Software Integration**: Many graphing software and image editors offer an option to export graphics directly into PDF format optimized for LaTeX, thereby streamlining the workflow.
    
    For these reasons, PDF is often the preferred choice for including images in LaTeX documents. However, depending on the specific needs of your project, other formats like PNG or JPG could also be suitable.
    

- [https://tex.stackexchange.com/questions/34732/latex-is-putting-a-border-around-my-figures](https://tex.stackexchange.com/questions/34732/latex-is-putting-a-border-around-my-figures)
    
    Not sure if this issue is still relevant with you, though, it happened to me with exported PDFs from Visio.
    
    It's quite a hidden problem until I found this [https://answers.microsoft.com/en-us/msoffice/forum/all/exported-visio-2016-drawing-to-pdf-has-an/63a74046-4010-4ae0-9c5e-329568361071](https://answers.microsoft.com/en-us/msoffice/forum/all/exported-visio-2016-drawing-to-pdf-has-an/63a74046-4010-4ae0-9c5e-329568361071)
    
    By default, exporting PDFs from Visio will have **Document structure tag for accessibility** option checked.
    
    So the fix is quite simple, just uncheck this option from the "Options..." dialog window opened from the export to pdf window.
    

Horitonztal line:

```latex
\noindent\makebox[\linewidth]{\rule{\paperwidth}{0.4pt}}
```

- NOTE: in overleaf, if use \hl on multiple lines, [page will reset to 0 in middle](https://tex.stackexchange.com/questions/284569/page-numbers-resets-to-0-at-the-beginning-of-a-chapter)

---

- how do I keep a figure in a section latex
    
    To ensure that a figure stays within a particular section in LaTeX, you can use the `placeins` package, which provides the `\\FloatBarrier` command. This command prevents floats from floating past it, effectively keeping them in the section.
    
    Here's how you can include it in your LaTeX document:
    
    1. Include the `placeins` package in your preamble.
    2. Place a `\\FloatBarrier` command either at the end of your section or right before the beginning of the next section.
    
    Here's an example:
    
    ```latex
    \\documentclass{article}
    \\usepackage{graphicx}
    \\usepackage{placeins} % Include the placeins package
    
    \\begin{document}
    
    \\section{First Section}
    
    % Your text here
    
    % Including a figure
    \\begin{figure}[htbp]
      \\centering
      \\includegraphics[width=0.8\\textwidth]{figure1.png}
      \\caption{This is the first figure}
      \\label{fig:figure1}
    \\end{figure}
    
    % Prevent floats from floating past this point
    \\FloatBarrier
    
    \\section{Second Section}
    
    % The rest of your document
    
    \\end{document}
    
    ```
    
    By placing `\\FloatBarrier` at the end of a section, you're ensuring that the figure placed in that section will not float into the following section. The `[htbp]` option with the `figure` environment is a suggestion to LaTeX about where to place the figure:
    
    - `h` (here) — at the location in the text where the figure environment appears.
    - `t` (top) — at the top of a text page.
    - `b` (bottom) — at the bottom of a text page.
    - `p` (page of floats) — on a separate float page, which is a page containing no text, only figures and tables.
    
    LaTeX will try to adhere to your placement specifications, but sometimes it may decide to move the figure to avoid unsightly empty spaces or overly cramped text. If you find that LaTeX is not placing the figure where you want it, you can try adjusting the figure's placement options or the figure's size, or you can work with the text around where the figure is placed to give LaTeX more flexibility in fulfilling your request.
# Notion

[https://cheatsheets.namaraii.com/notion.html](https://cheatsheets.namaraii.com/notion.html)

---

To quickly navigate to a page, instead of using the left-pane tree dir, just type “@ page” and ctrl+click to open a new tab. Then delete this link.

---

Q: Why are some pages not aligned with others? It seems like there’s a space in front:

![Untitled](Notion%2003b683dc0d694a6c863be959c6458bb7/Untitled.png)

- SOLN
    
    A: The pages like test with no space in front are in-line links created using “[[”. The other pages are page-line and were created by the “+” button, or highlighting the entire line and “turning it from text to page”. You cannot write any other text on a “page-line” link.
    
    The preference, for consistency, is to use page-line whenver you mean for just a page, and in-line only when you need to write other things on it.
    
    <<<
    
    NOTE: a page created by turning text into page cannot be dragged into another page created by “[[” as a sub-page. However, pages created by [[ can be dragged into pages created by both ways. So [[ may be preferred for versatility
    
    This may because pages created “page-line” have a strict nested hierarchical structure? No, that doesn’t make sense b/c they can be dragged into other pages if those other pages were created the same way
    
    For example, you can drag test2 (inline) into test (page-line), but not test into test2:
    
    [test](Notion%2003b683dc0d694a6c863be959c6458bb7/test%201c269f811c024a69be0770febc4a04e4.md)
    
    [test2](Notion%2003b683dc0d694a6c863be959c6458bb7/test2%20ce27bed53a514439b430b730edbae93d.md) 
    
    So inline is more flexible. However, it causes a ‘loading screen’ where you can’t create a “new page” until it’s finished loading, else you risk hitting an option of an existing page when it loads and re-arrages where you cursor appears on. So page-line may be faster if there are many matches to load.
    
    Also, page-line doesn’t go to next line:
    
    ![Untitled](Notion%2003b683dc0d694a6c863be959c6458bb7/Untitled%201.png)
    
    One advantage of page line, however, is that it is easier to use. [[ may “cancel” becoming a page if you make changes when writing it. In any case, the alignment is not that important.
    
    <<<
    
    Neither type of page can be dragged and dropped into another root super-notebook. However, both types can be dragged into any sub-notebooks of a super-notebook
    

If you copy one page inside another, its backlinks won’t be copied.

DANGER: DO NOT TURN AN IN-LINE PAGE FROM TEXT TO ‘PAGE’; IT WILL DELETE ALL IN THE PAGE

---

[https://www.wepc.com/tips/chat-gpt-vs-notion-ai/](https://www.wepc.com/tips/chat-gpt-vs-notion-ai/)

Notion Ai uses the GPT 3 API, and ChatGPT uses GPT 3.5

ChatGPT is more suitable for tasks that require a broad range of knowledge and [natural language processing](https://www.wepc.com/tips/is-chat-gpt-a-language-model-or-a-conversational-ai/), such as content creation and customer service. On the other hand, Notion AI is more suitable for tasks within the Notion platform, such as automating the creation of pages, tables, and databases.

Users can train Notion AI to recognize specific keywords and provide relevant suggestions based on their preferences. This level of customization is particularly useful for teams with specific workflows and requirements

---

Dragging to select multiple lines often overlaps with unwanted selections. For more precise selection, click on a line and click again while holding shift. If on a numbered section, hover over the number until the entire section is blue, and click to drag.

---

To turn something into red code inline: use SINGLE ` to close words. Or highlight and ctrl + e

---

BACKLINKS: These only occur if you use “@ page”, but cannot occur if you highlight a phrase and add a link to it. However, “@ page” doesn’t allow you to customize the phrase to the link.

---

To quickly use toggle, /tog then write in header, and enter to next line, then just tab in (backspace if it creates new toggle bullet). Alt, click the arrow and click in the body.

To quickly put something copied w/ both header and body in toggle, use /tog then paste both header and body inside. Then just backspace header in, and tab body in.

---

In line equations: first must start with $$, then end with $$. If don’t start with $$ when typing it, it won’t work. To force what’s inside as an equation, using brackets: $${ }$$

---

Alt + enter makes less of a line space than enter

---

When exporting, only pages with pages within will be turned into folders (else they’ll just be files). Colons (:), etc in names will just be removed in files/folders names

---

To quickly use emojis in text, use “/emo”

---

test [one two](https://www.notion.so/one-two-c58906e250cd409fb78e59293a340598?pvs=21) three

[https://www.reddit.com/r/Notion/comments/pz7cts/is_there_no_simple_way_to_add_tags_to_pages/](https://www.reddit.com/r/Notion/comments/pz7cts/is_there_no_simple_way_to_add_tags_to_pages/)

---

When making a two col after another two col, just drag below into next row of col isntead of making new two col. Making a new one will create a smaller ‘two col within two col’

---

- in notion I have authors and papers. i want two page dbs: authors and papers. the papers db has authors as a col, and authors has papers as col. how do I get an author as an entity with its own properties (list of papers, etc) and link them to the papers db
    
    To achieve the structure you're describing in Notion, where you have two databases—one for authors and one for papers—with the ability to link papers to authors and vice versa, you can follow these steps. This will allow each author to have their own page with properties (like a list of papers they've authored) and similarly for papers to reference their authors.
    
    ### 1. Create the Authors Database
    
    1. **Create a New Page**: In Notion, create a new page where you want your database to reside.
    2. **Add Database**: Choose to add a database to your page, selecting the "Table" format.
    3. **Name Your Database**: Name it "Authors".
    4. **Define Properties**: In your Authors database, define properties that you would like to track for each author (e.g., Name, Affiliation, Field of Study).
    
    ### 2. Create the Papers Database
    
    1. **Create a Second New Page**: Similar to the first, create another new page for your second database.
    2. **Add Database**: Add another database, again selecting the "Table" format.
    3. **Name Your Database**: Name this one "Papers".
    4. **Define Properties**: Define the properties for your Papers database (e.g., Title, Publication Date, Abstract).
    5. **Add Authors Relation**: Add a new property, and select the type as "Relation". You will be prompted to choose which database you want to create a relation with. Select your Authors database. This creates a two-way relation between each paper and its authors.
    
    ### 3. Create the Relation Back from Authors to Papers
    
    1. **Navigate Back to Authors Database**: Go back to your Authors database. You should see a new property automatically created that represents the relation to the Papers database.
    2. **Rename the Property (Optional)**: Notion will give this property a default name, but you can rename it to something more descriptive, like "Papers Written".
    
    ### 4. Linking Papers to Authors
    
    Whenever you add a new paper to the Papers database:
    
    1. **Fill in the Paper Details**: Enter the details for your paper.
    2. **Select the Author(s)**: In the authors relation column, click to select the author(s) of the paper. You can select multiple authors if necessary.
    
    ### 5. Viewing an Author's Papers
    
    When you open an author's page within the Authors database:
    
    1. **View the Linked Papers**: You will see a linked database or list showing all the papers connected to that author.
    2. **Customize the View**: You can customize how this linked list or database looks, showing only certain columns, filtering or sorting the papers, etc.
    
    ### 6. Additional Customizations
    
    - **Bi-directional Updates**: Thanks to the relation, adding a paper to an author or an author to a paper will reflect on both databases.
    - **Advanced Views**: You can create different views (e.g., filtered, sorted, as a calendar) in both databases to manage and visualize the data more effectively.
    - **Page Content**: Each author and paper can have its own page where you can add additional content, like an extended bio for an author or full paper text and figures for a paper.
    
    By setting up your Notion workspace in this way, you create a dynamic and interconnected system where authors and their publications are easily managed, tracked, and cross-referenced.
    

To link two db in notion, you must create a new relation and set the option “Show on [DB 2]” on in ‘edit properties’. If it’s not showing, delete the current relation and create a new one with this option. Make sure BOTH (or more) tables link to one another (invertible?) Then if you remove an author from a paper in the paper db, the author db will remove that paper from the paper relation.

NOTE: if you find editing paper db’s author property will edit author db; editing author db’s paper property may not have paper db author property be updated. just wait or refresh.
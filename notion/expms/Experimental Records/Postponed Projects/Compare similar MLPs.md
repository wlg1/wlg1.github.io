# Compare similar MLPs

- Write a plan to compare the neuron activations of multiple similar, simple models to find similar activation circuits
    
    Title: Comparing Neuron Activations in Similar, Simple Models to Identify Similar Activation Circuits
    
    Objective:
    The aim of this project is to compare the neuron activations of multiple similar, simple models to find similar activation circuits. By identifying these circuits, we can gain insights into the underlying mechanisms that drive the models' performance and potentially improve their functionality.
    
    1. Selection of Models:
    a. Choose a set of simple models with similar architecture and trained on similar tasks (e.g., image classification or text analysis).
    b. Ensure the models have adequate documentation, including their architecture, training data, and performance metrics.
    2. Data Preparation:
    a. Select a diverse set of inputs that cover various aspects of the models' tasks (e.g., different categories of images or a variety of text samples).
    b. Preprocess the data to ensure compatibility with the selected models (e.g., resizing images or tokenizing text).
    3. Model Activation Analysis:
    a. Implement a method to extract neuron activation values at each layer of the models.
    b. Apply this method to each model while processing the prepared dataset.
    c. Record the neuron activation values for each input and layer in the models.
    4. Activation Circuit Comparison:
    a. Identify groups of neurons that consistently activate together across the models. These can be considered as activation circuits.
    b. Use similarity metrics (e.g., cosine similarity or correlation coefficients) to compare the activation patterns of these circuits across different models.
    c. Create a similarity matrix to visualize the relationships between activation circuits.
    5. Interpretation and Visualization:
    a. Analyze the activation circuits to identify common patterns or differences between the models.
    b. Visualize the activation circuits using dimensionality reduction techniques (e.g., t-SNE or UMAP) to facilitate interpretation.
    c. Relate the activation circuits to the models' performance metrics and their underlying tasks.
    6. Model Improvement:
    a. Based on the analysis of the activation circuits, suggest potential improvements to the models, such as modifying their architecture or hyperparameters.
    b. Implement these improvements and retrain the models.
    c. Evaluate the modified models using the original performance metrics and compare them to the initial models.
    7. Documentation and Reporting:
    a. Document the entire process, including the selection of models, data preparation, activation analysis, and interpretation.
    b. Report the findings, including the identified activation circuits, their similarities and differences, and the potential improvements for the models.
    c. Share the results with the research community and the developers of the models to contribute to the understanding of neural networks and their optimization.
    8. Future Work:
    a. Explore the applicability of the identified activation circuits to more complex models or different tasks.
    b. Investigate the possibility of transferring the activation circuits between models to improve their performance.
    c. Further refine the analysis and visualization techniques to better understand the activation circuits and their role in model performance.

[https://colab.research.google.com/drive/1psDYCAvhNUwXvnBSixYU58_uEhkiLfzL#scrollTo=fgu21_asJyZd](https://colab.research.google.com/drive/1psDYCAvhNUwXvnBSixYU58_uEhkiLfzL#scrollTo=fgu21_asJyZd)

- Convert step 1 into python code
    
    ```python
    import torch
    import torchvision.models as models
    
    # Step 1: Selection of Models
    
    def load_pretrained_models(model_names):
        """
        Load pretrained models based on the given model names.
    
        Args:
            model_names (list): A list of strings representing the names of the models to load.
    
        Returns:
            model_dict (dict): A dictionary containing the loaded models with their names as keys.
        """
    
        model_dict = {}
        for model_name in model_names:
            try:
                model = getattr(models, model_name)(pretrained=True)
                model_dict[model_name] = model
                print(f"{model_name} loaded successfully.")
            except AttributeError:
                print(f"{model_name} not found in torchvision.models.")
            except Exception as e:
                print(f"Error loading {model_name}: {e}")
    
        return model_dict
    
    # Example: Load three similar models
    model_names = ['resnet18', 'resnet34', 'resnet50']
    models_dict = load_pretrained_models(model_names)
    
    ```
    
    This code snippet demonstrates how to load three similar pretrained models (ResNet18, ResNet34, and ResNet50) using PyTorch and torchvision. The `load_pretrained_models` function takes a list of model names and returns a dictionary containing the loaded models. You can modify the `model_names` list to include other models based on your requirements. Note that this example assumes you are using PyTorch and torchvision and have already installed them.
    
- 2
    
    ```
    import torchvision.transforms as transforms
    from torchvision.datasets import ImageFolder
    from torch.utils.data import DataLoader
    
    # Step 2: Data Preparation
    
    def preprocess_data(data_path, input_size, batch_size):
        """
        Preprocess the data and create a DataLoader.
    
        Args:
            data_path (str): Path to the dataset folder containing subfolders for each class.
            input_size (tuple): The size of the input images (width, height).
            batch_size (int): The number of samples per batch during data loading.
    
        Returns:
            data_loader (DataLoader): A DataLoader for the preprocessed dataset.
        """
        transform = transforms.Compose([
            transforms.Resize(input_size),
            transforms.CenterCrop(input_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
    
        dataset = ImageFolder(root=data_path, transform=transform)
        data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=2)
    
        return data_loader
    
    # Example: Preprocess data and create a DataLoader
    data_path = "/path/to/your/dataset"
    input_size = (224, 224)
    batch_size = 32
    
    data_loader = preprocess_data(data_path, input_size, batch_size)
    
    ```
    
    This code snippet demonstrates how to preprocess a dataset of images and create a DataLoader using torchvision. The `preprocess_data` function takes the path to the dataset folder, the input size for the images, and the batch size for the DataLoader. The function returns a DataLoader for the preprocessed dataset. Modify the `data_path` variable to point to the directory containing your dataset. Note that this example assumes you are using torchvision and have already installed it.
    
- 3
    
    ```
    import numpy as np
    
    # Step 3: Model Activation Analysis
    
    def hook_fn(module, input, output, activations, layer_name):
        """
        Hook function to extract neuron activation values.
    
        Args:
            module (torch.nn.Module): The hooked module.
            input (tuple): Input tensor(s) to the module.
            output (tensor): Output tensor from the module.
            activations (dict): Dictionary to store the activation values.
            layer_name (str): Layer name to be used as key in the activations dictionary.
        """
        activations[layer_name] = output.detach().numpy()
    
    def register_hooks(model, activations):
        """
        Register hooks to extract neuron activation values at each layer.
    
        Args:
            model (torch.nn.Module): The model for which hooks are to be registered.
            activations (dict): Dictionary to store the activation values.
        """
        for name, module in model.named_modules():
            module.register_forward_hook(lambda module, input, output: hook_fn(module, input, output, activations, name))
    
    def extract_activations(models_dict, data_loader):
        """
        Extract neuron activation values for each model and input in the data_loader.
    
        Args:
            models_dict (dict): A dictionary containing the models with their names as keys.
            data_loader (DataLoader): A DataLoader for the preprocessed dataset.
    
        Returns:
            activations_dict (dict): A dictionary containing the activation values for each model and input.
        """
        activations_dict = {}
    
        for model_name, model in models_dict.items():
            model.eval()
            activations = {}
            register_hooks(model, activations)
    
            model_activations = []
    
            with torch.no_grad():
                for inputs, _ in data_loader:
                    outputs = model(inputs)
                    model_activations.append(activations.copy())
    
            activations_dict[model_name] = model_activations
    
        return activations_dict
    
    # Example: Extract neuron activations for each model and input
    activations_dict = extract_activations(models_dict, data_loader)
    
    ```
    
    This code snippet demonstrates how to extract neuron activations for each model and input in the data_loader. The `hook_fn` function is a hook that extracts activation values from the layers, and the `register_hooks` function registers these hooks for all layers in a given model. The `extract_activations` function iterates over the provided models and data_loader, applying the hooks and storing the activation values in the `activations_dict` dictionary. The example at the end of the code snippet shows how to call `extract_activations` with the `models_dict` and `data_loader` created in the previous steps.
    
- 4
    
    ```
    from sklearn.metrics.pairwise import cosine_similarity
    
    # Step 4: Activation Circuit Comparison
    
    def identify_activation_circuits(activations_dict, similarity_threshold=0.8):
        """
        Identify groups of neurons that consistently activate together across the models.
    
        Args:
            activations_dict (dict): A dictionary containing the activation values for each model and input.
            similarity_threshold (float): The threshold for cosine similarity to consider neurons as part of the same circuit.
    
        Returns:
            circuits_dict (dict): A dictionary containing the identified activation circuits for each model.
        """
        circuits_dict = {}
    
        for model_name, model_activations in activations_dict.items():
            circuits = []
    
            for layer_name, layer_activations in model_activations[0].items():
                layer_circuits = []
    
                for i in range(layer_activations.shape[1]):
                    circuit = [i]
                    for j in range(i + 1, layer_activations.shape[1]):
                        similarity = cosine_similarity(layer_activations[:, i].reshape(1, -1),
                                                        layer_activations[:, j].reshape(1, -1))
                        if similarity >= similarity_threshold:
                            circuit.append(j)
    
                    layer_circuits.append(circuit)
    
                circuits.append(layer_circuits)
    
            circuits_dict[model_name] = circuits
    
        return circuits_dict
    
    # Example: Identify activation circuits in the models
    similarity_threshold = 0.8
    circuits_dict = identify_activation_circuits(activations_dict, similarity_threshold)
    
    ```
    
    This code snippet demonstrates how to identify groups of neurons that consistently activate together across the models. The `identify_activation_circuits` function takes the `activations_dict` obtained in step 3 and a similarity_threshold. It computes the cosine similarity between neuron activations and identifies activation circuits based on the provided threshold. The function returns a dictionary containing the identified activation circuits for each model. The example at the end of the code snippet shows how to call `identify_activation_circuits` with the `activations_dict` created in step 3 and a similarity threshold of 0.8.
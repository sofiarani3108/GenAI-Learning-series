# Week 6: Open-Source Models & Fine-Tuning (Advanced)

## Focus

This week focuses on working with open-source LLMs instead of only commercial APIs.

Key topics:

- Open-source models (Llama, Mistral)
- Hugging Face model and dataset workflows
- Parameter-efficient fine-tuning (PEFT)
- QLoRA for low-cost GPU training
- Model quantization for smaller memory use
- Domain-specific tone and output formatting

## Weekly Project

### Fine-Tuned Small Language Model (SLM) for a Specific Domain

Build a small fine-tuning workflow that teaches an open-source model to follow a specific writing style, industry jargon, or structured output format.

Example use cases:

- Customer support replies in company tone
- Incident reports in a fixed template
- Finance summaries using internal terminology
- JSON or markdown outputs in a strict format

## What You Need To Do

- Collect or create a small training dataset
- Clean and format the data consistently
- Choose a base model such as **Llama 3 8B** or **Mistral 7B**
- Fine-tune the model using **QLoRA** in Google Colab or a cloud GPU
- Test whether the model follows the target tone or format
- Compare base model vs fine-tuned model outputs
- Save the adapter or model artifacts for reuse

## Dataset Requirements

Your dataset should teach one clear behavior.

Good examples:

- Input text → desired formatted response
- User question → company-style answer
- Raw notes → structured report

Recommended format:

```json
{
  "instruction": "Rewrite this customer message in company support tone.",
  "input": "My payment failed twice.",
  "output": "Thank you for reaching out. We understand how frustrating duplicate charges can be..."
}
```

Aim for:

- 100 to 500 high-quality examples for a first version
- Consistent formatting across all rows
- Real domain language instead of generic text

## Suggested Workflow

1. Define the target style or output format
2. Prepare and validate the dataset
3. Load a base open-source model from Hugging Face
4. Apply QLoRA adapters
5. Fine-tune on GPU
6. Run inference on sample prompts
7. Compare results with the base model
8. Save the trained adapter and document findings

## Suggested Folder Structure

```text
Week6/
├── projectReadme.md
├── notebook/
│   └── finetune_qlora.ipynb
├── data/
│   ├── train.jsonl
│   ├── eval.jsonl
│   └── samples/
├── prompts/
│   └── test_prompts.txt
├── outputs/
│   ├── base_model_samples.md
│   └── finetuned_model_samples.md
└── requirements.txt
```

## Tools To Use

- Hugging Face Transformers
- Hugging Face Datasets
- PEFT
- bitsandbytes
- TRL or similar training utilities
- Google Colab or another GPU environment

## Deliverables

- Training dataset in a clean instruction format
- Colab notebook or training script for QLoRA fine-tuning
- Fine-tuned adapter or model checkpoint
- Before/after output comparison
- Short notes on what improved and what did not

## Success Criteria

The project is successful when the fine-tuned model:

- Follows the target tone better than the base model
- Produces more consistent structured outputs
- Uses domain-specific language correctly
- Generalizes to new prompts not seen in training

## Practical Tips

- Start with a very small dataset and verify the pipeline works
- Keep one task per fine-tuning run
- Use evaluation prompts that were not included in training
- Track GPU memory, training time, and loss
- Do not expect perfect results from a tiny dataset

## Stretch Ideas

- Add evaluation metrics for format accuracy
- Compare Llama vs Mistral on the same dataset
- Export the model for local inference
- Build a simple Streamlit demo for side-by-side comparison

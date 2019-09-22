# Elevate Tech Jam Hackathon: Dollar Bytes

## About

This repository contains the submission for the [Elevate](https://elevate.ca/) [Tech Jam Hackathon](https://elevate-tech-jam-2019.devpost.com/) from Team Dollar Bytes.

## Product Design

**TD RiseUpTogether** is a TD-facilitated marketplace that allows young entrepreneurs looking for funding & sponsorship and elderly seniors looking to invest and mentor young entrepreneurs to be matched.

Through the use of this platform, young enterpreneurs have access not only to another source of funding, but more importantly, mentorship from well-experienced people in their communities. The would-be investors will have a locally-growing place for small-scale investment, but more importanly, an avenue to put their wealth (pun intended!) of experience into use through mentoring young enterpreneurs in the community.

Access our [Google Drive folder](https://drive.google.com/drive/folders/1k-GUqhaakyFdbbpEd-UDQUVAUukxWryG) for:
 - A presentation slide to describe our solution
 - Prototype, in Sketch
 - Video demos

## Data Analysis

As part of the Hackathon, TD provides a dataset of thousands of realistic virtual customers and their financial information, accessible through a RESTful API (link to [TD Da Vinci](https://td-davinci.com/)).

### Data extraction

Data extraction is accomplished through a [group of Python scripts](src/data/) running on multiple AWS EC2 t3.micro instances. The following information were captured:

 - Raw data of virtual customers, through the [RawData](https://td-davinci.com/documents/raw-data) endpoint: basic demographic data, location of their principal residence, total annual income, etc.
 - Customer bank account and credit card balances, through the [Account](https://td-davinci.com/documents/account) endpoint: deposit, chequing, and credit card accounts
 - Select customers' transaction data, through the [Transaction](https://td-davinci.com/documents/transaction) endpoint.

The API responses are captured and stored as individual JSON files without transformation.

### Data analysis

JSONs are consolidated into CSV files before loading to a local PostgreSQL database with PostGIS extension. As examples, following queries were developed:

 - Descriptive statistics on the virtual customers' demographics
 - Find the list of virtual customers with bank account balances exceeding a certain threshold
 - Given a would-be investor's location, find the list of would-be young entrepreneurs and sort by geographical proximity

## Team

Dollar Bytes is a project team for the Hackathon, comprised of:
 - Anne-Marie Bourgeois
 - Tanya Matanda
 - David Lee
 - Manuel S. Sardon
 - Kyle Pearce
# Travel Suggestion Agent using MCP + ADK

## Problem Statement
Build an AI agent that connects to external tools using MCP.

## Solution
This project builds a travel suggestion agent that fetches real-time place data using Google Places API via an MCP server.

## Architecture
User → Agent → MCP Server → Google Places API

## Features
- Suggests cafes, restaurants, tourist places
- Uses MCP for tool integration
- Deployed on Cloud Run

## Example
Input:
"Best cafes in Mumbai"

Output:
- Cafe A ⭐ 4.5 - Bandra
- Cafe B ⭐ 4.6 - Andheri
